'use strict';
var scss          = require('postcss-scss');
var safe          = require('postcss-safe-parser');
var stdin         = require('get-stdin');
var postcss       = require('postcss');
var perfectionist = require('perfectionist');

stdin(function(data) {
  var opts = JSON.parse(process.argv[2]);

  postcss([perfectionist(opts)])
    .process(data, {
      syntax: scss
    })
    .then(function(result) {
      process.stdout.write(result.css);
    }).catch(function(err) {
      if (err.name === 'CssSyntaxError') {
        err.message += '\n' + err.showSourceCode();
      }

      console.error(err.message.replace('<css input>:', ''));
    });

});
