
/*
 * For index.html, build single CSS file with clean-css
 * input files need be hand write to cssFileHash in the below
 * same as output file
 */

var fs = require('fs');
var path = require('path');

var CleanCSS = require('clean-css');

var p = console.log;


var template_dir = path.join(__dirname, "../template");
var node_modules_dir = path.join(__dirname, "../node_modules");
//p(template_dir, "\r\n", node_modules_dir);

var outputFile = path.join(template_dir, "bundle.index.css");


var normalize_css = path.join(node_modules_dir, "normalize.css/normalize.css");
var skeleton_css = path.join(node_modules_dir, "skeleton-css/css/skeleton.css");
var my_old_css = path.join(template_dir, "style/src/old.index.css");




var cssFileHash = {
    '../node_modules/normalize.css/normalize.css': {
        'styles': fs.readFileSync(normalize_css, 'utf8')},

    '../node_modules/skeleton-css/css/skeleton.css': {
        'styles': fs.readFileSync(skeleton_css, 'utf8')},

    './style/src/old.index.css': {
        'styles': fs.readFileSync(my_old_css, 'utf8')}
};



// give the Hash of css files, .minify() will concatenate them to single output.
// 0820

//p(process.cwd());
//p(Object.keys(cssFileHash), "\r\n", outputFile);
var m = new CleanCSS({
    inline:['all'],
    format:'beautify'
}).minify(cssFileHash, (err, minified)=>{
    if(err){return p('.minify err: ', err);}

    //p('before write');
    ////p(minified);
    fs.writeFile(outputFile, minified.styles, 'utf8', (err)=>{
        if(err) return console.log('write err', err);

        return ;//p(outputFile, ' should be written');
    });

});






