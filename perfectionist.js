'use strict';
var stdin = require('get-stdin');
var postcss = require('postcss');
var perfectionist = require('perfectionist');

stdin(function(data) {
  var opts = JSON.parse(process.argv[2]);

  postcss()
    .use(perfectionist(opts))
    .process(data, {
      safe: true
    })
    .then(function(res) {
      process.stdout.write(res.css);
    }).catch(function(err) {
      if (err.name === 'CssSyntaxError') {
        err.message += '\n' + err.showSourceCode();
      }

      console.error(err.message.replace('<css input>:', ''));
    });
});
