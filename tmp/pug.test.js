
const fs = require("fs");

var pug = require('pug');

const p = console.log;

// compile
var options = {};
var locals = {};
var fn = pug.compile('string of pug', options);
var html = fn(locals);
p(1, html);

//// render
//var html = pug.render('string of pug', merge(options, locals));
//p(2, html);
//
//// renderFile
//var html = pug.renderFile('filename.pug', merge(options, locals));
//p(3, html);
