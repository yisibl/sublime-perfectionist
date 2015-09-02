import sublime
import sublime_plugin
import os
import re
import json
from os.path import dirname, realpath, join

try:
    # Python 2
    from node_bridge import node_bridge
except:
    from .node_bridge import node_bridge

# monkeypatch `Region` to be iterable
sublime.Region.totuple = lambda self: (self.a, self.b)
sublime.Region.__iter__ = lambda self: self.totuple().__iter__()

BIN_PATH = join(sublime.packages_path(), dirname(
    realpath(__file__)), 'perfectionist.js')


class PerfectionistCommand(sublime_plugin.TextCommand):

    def run(self, edit, action='expanded'):
        if action == 'auto':
            action = self.get_setting('format')

        if not self.has_selection():
            region = sublime.Region(0, self.view.size())
            originalBuffer = self.view.substr(region)
            code = self.beautify(originalBuffer, action)
            if code:
                self.view.replace(edit, region, code)
            return
        for region in self.view.sel():
            if region.empty():
                continue
            originalBuffer = self.view.substr(region)
            code = self.beautify(originalBuffer, action)
            if code:
                self.view.replace(edit, region, code)

    def beautify(self, data, action):
        try:
            return node_bridge(data, BIN_PATH, [json.dumps({
                'format': action,
                'indentSize': self.get_setting('indent_size'),
                'cascade': self.get_setting('cascade'),
                'maxAtRuleLength': self.get_setting('max_at_rule_length'),
                'maxSelectorLength': self.get_setting('max_selector_length'),
                'maxValueLength': self.get_setting('max_value_length')
            })])
        except Exception as e:
            sublime.error_message('Perfectionist\n%s' % e)

    def has_selection(self):
        for sel in self.view.sel():
            start, end = sel
            if start != end:
                return True
        return False

    def get_setting(self, key):
        settings = self.view.settings().get('perfectionist')
        if settings is None:
            settings = sublime.load_settings('perfectionist.sublime-settings')
        return settings.get(key)

    # Filter file
    def is_visible(self):
        view = self.view
        file_name = view.file_name()
        syntax_path = view.settings().get('syntax')
        suffix_array = self.get_setting('file_filter').split(',')
        suffix = ''
        syntax = ''

        if file_name != None:  # file exists, pull syntax type from extension
            suffix = os.path.splitext(file_name)[1][1:]
        if syntax_path != None:
            syntax = os.path.splitext(syntax_path)[0].split('/')[-1].lower()
        return suffix in suffix_array or syntax in suffix_array

# On Save File auto format
class BeautifyOnSave(sublime_plugin.EventListener):

    def on_pre_save(self, view):
        settings = sublime.load_settings('perfectionist.sublime-settings')

        should_format = view.settings().get(
            'format_on_save', settings.get('format_on_save', False))
        if not should_format:
            return

        file_filter_list = view.settings().get('file_filter', settings.get(
            'file_filter', 'css,scss,less,html,htm')).replace(',', '|')
        filter_region_concat = '\.(' + file_filter_list + ')$'

        if not re.search(filter_region_concat, view.file_name()):
            return

        format_action = view.settings().get(
            'format', settings.get('format', 'expanded'))
        if not format_action:
            return

        view.run_command('perfectionist', {'action': format_action})
