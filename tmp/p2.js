
const fs = require("fs");

var pug = require('pug');

const p = console.log;

fs.readFile('./test.pug', 'utf-8', function(err, text){
    //p(err, text);
    var html = pug.render(text, {pretty: true});
    p('html');
    p(html);
    fs.writeFile('./tmp.html', html, function(err){
        if(err) p('write file err? ', err);
        p('write file finished');
    });
});
