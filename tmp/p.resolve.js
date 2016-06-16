
var url  = require('url');
var path = require('path');

var p = console.log;

function resolve(file_path, href){
    var dname = path.dirname(file_path);

    var joined = path.join(dname, href);
    var result = path.normalize(joined);

    return result;
}

window.presolve = resolve;


function uresolve(current_file_path, href){
    return url.resolve(current_file_path, href);
}

window.uresolve = uresolve;


function look_like_markdown(href){
    var parsed = url.parse(href);

    var ppath = href;
    if(parsed.path) ppath = parsed.path;

    var lpath = ppath.toLowerCase();

    if(lpath.endsWith('md')) return true;
    if(lpath.endsWith('markdown')) return true;
    return false;
}

window.look_like_markdown = look_like_markdown;

