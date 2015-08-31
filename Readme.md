# sublime-perfectionist

> A Powerful Sublime Text plugin to beautify your CSS!

Powered by [perfectionist](https://github.com/ben-eb/perfectionist)


![screenshot](shot.gif)

**Input:**

```css
/*sublime-perfectionist test*/
@media screen {
.foo { & > .bar {
  -webkit-transform: scale(0);/*commment*/
  -ms-transform: scale(0);-o-transform: scale(0);
  transform: scale(0);}}
}
```

**Output:**

```css
/*sublime-perfectionist test*/

@media screen {
  .foo {
    & > .bar {
      -webkit-transform: scale(0); /*commment*/
          -ms-transform: scale(0);
           -o-transform: scale(0);
              transform: scale(0);
    }
  }
}
```

## Installation

**First of all, you need to have Node.js installed.**

Make sure it's in your `$PATH` by running `node -v` in your command-line.

> Note: On OS X it's expected that Node should reside in the `/usr/local/bin/` folder, 
which it does when installed with the default installer. If this is not the case,
symlink your Node binary to this location. For example, if you used nvm:  
`ln -s -f /Users/#{username}/.nvm/versions/#{nodeVersion}/bin/node /usr/local/bin/node`  
See also: http://weibo.com/1397442732/BA52YbcdG

### Method 1: Install from GitHub

1. Run the following command in your Sublime Text packages directory 
```
$ git clone https://github.com/yisibl/sublime-perfectionist perfectionist
```

2. Depending on your OS (and Sublime Text version) the packages directories are:

  * Windows: `cd %APPDATA%\Sublime Text 3\Packages`
  * OS X: `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages`
  * Linux: `cd ~/.config/sublime-text-3/packages`

### Method 2: Download

1. Download the source zip from Github.
2. Open Sublime Text menu `Preferences > Browse Packages`.
3. Extract it into a new folder named 'perfectionist' in your Sublime Text "Packages" folder.
4. Restart Sublime Text.


## Usage

1. Open the Command Palette: `Cmd+Shift+P`(OSX) or `Ctrl+Shift+P`(Linux/Window).
2. Choose: `CSS Perfectionist`, or use the shortcut keys `Cmd+Shift+E`(OS X)/`Ctrl+Shift+E`(Linux/Window).

## Options

`Preferences` > `Package Settings` > `Perfectionist` > `Settings - User`

## Acknowledgements

This plugin is based on the excellent [Autoprefixer plugin](https://github.com/sindresorhus/sublime-autoprefixer) by Sindre Sorhus.

Thank [@Ovilia](https://github.com/Ovilia/) for reviewing the document.

* [如何开发Sublime Text2插件](http://www.welefen.com/how-to-develop-sublime-text-plugin.html)
* [sublime插件开发手记](http://www.hickwu.com/sublime%E6%8F%92%E4%BB%B6%E5%BC%80%E5%8F%91%E6%89%8B%E8%AE%B0)
* [Sublime插件API手册 ](http://mux.alimama.com/posts/549)
* [sublime插件开发](http://mux.alimama.com/posts/541)

## License

MIT © [yisibl](https://github.com/yisibl/) ([Weibo](http://weibo.com/jieorlin))
