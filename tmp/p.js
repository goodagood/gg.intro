
var path = require('path');
var url  = require('url');

var p = console.log;

function resolve(current_file_path, href){
    var dname = path.dirname(current_file_path);

    var joined = path.join(dname, href);
    var result = path.normalize(joined);

    return result;
}


function uresolve(current_file_path, href){
    return url.resolve(current_file_path, href);
}


function look_like_markdown(href){
    var parsed = url.parse(href);

    var ppath = href;
    if(parsed.path) ppath = parsed.path;

    var lpath = ppath.toLowerCase();

    if(lpath.endsWith('md')) return true;
    if(lpath.endsWith('markdown')) return true;
    return false;
}



// -- for checkings

if(require.main === module){
    p(resolve('./general/abc.md', 'def.md'));


    var file_path = './general/intro.md';
    var href = '../another/start.md';


    var dname = path.dirname(file_path);
    var dname_parsed = path.parse(file_path);

    var dname_normalized = path.normalize(dname);

    var res = path.resolve(dname, href);
    var rel = path.relative(dname, href);

    var jed  = path.join(dname, href);
    var njed = path.normalize(jed);

    var aa = path.relative(dname_normalized, res);
    console.log('jed: ', jed);
    console.log('njed: ', njed);
}
