

/*
 * 2018 0831
 */

var fs   = require('fs');
var path = require('path');

var p = console.log;


var outputFile = "../template/bundle.css";



p('__dirname', __dirname, '  __filename: ', __filename)


var tempdir = path.join(__dirname, '../template')
var styledir = path.join(__dirname, '../template/style')

p('template dir: ', tempdir)
p('style dir: ', styledir)
