
/*
 * Build single CSS file with clean-css
 */

var fs = require('fs');

var CleanCSS = require('clean-css');

var p = console.log;


var outputFile = "bundle.css";
var cssFile    = "./public/src/a.css";

var cssFileHash = {
    '../node_modules/normalize.css/normalize.css': {
        'styles': fs.readFileSync('../node_modules/normalize.css/normalize.css', 'utf8')},

    './style/index.css':        {'styles': fs.readFileSync('./style/index.css', 'utf8')}
};



// give the Hash of css files, .minify() will concatenate them to single output.
// 0820

var m = new CleanCSS({
    inline:['all'],
    format:'beautify'
}).minify(cssFileHash, (err, minified)=>{
    if(err){return p('.minify err: ', err);}

    p('before write');
    //p(minified);
    fs.writeFile(outputFile, minified.styles, 'utf8', (err)=>{
        if(err) console.log('write err', err);
    });

});






