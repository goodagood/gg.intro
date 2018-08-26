
/*
 * For index.html, build single CSS file with clean-css
 * input files need be hand write to cssFileHash in the below
 * same as output file
 */

var fs = require('fs');

var CleanCSS = require('clean-css');

var p = console.log;


var outputFile = "index.bundle.css";
//var cssFile    = "./public/src/a.css";

var cssFileHash = {
    '../node_modules/normalize.css/normalize.css': {
        'styles': fs.readFileSync('../node_modules/normalize.css/normalize.css', 'utf8')},

    '../node_modules/skeleton-css/css/skeleton.css': {
        'styles': fs.readFileSync('../node_modules/skeleton-css/css/skeleton.css', 'utf8')},

    './style/src/old.index.css': {
        'styles': fs.readFileSync('./style/src/old.index.css', 'utf8')}
};



// give the Hash of css files, .minify() will concatenate them to single output.
// 0820

p(process.cwd());
p(Object.keys(cssFileHash), "\r\n", outputFile);
var m = new CleanCSS({
    inline:['all'],
    format:'beautify'
}).minify(cssFileHash, (err, minified)=>{
    if(err){return p('.minify err: ', err);}

    p('before write');
    ////p(minified);
    fs.writeFile(outputFile, minified.styles, 'utf8', (err)=>{
        if(err) return console.log('write err', err);

        return p(outputFile, ' should be written');
    });

});






