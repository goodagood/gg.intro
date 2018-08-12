

var Color = require("color");

const coo = require("./cookie.js");


const BLACK = '#000000';
const WHITE = '#FFFFFF';

//window.Color = Color;


// 3 aa-large 4.5 aa 7 aaa 21


// 2017 1016



function bodyColor(foreground, background){
    foreground = foreground || BLACK;
    background = background || WHITE;

    document.body.style.color = foreground;
    document.body.style.backgroundColor = background;

    coo.setCookie('fgcolor', foreground, 365)
    coo.setCookie('bgcolor', background, 365)
}


function colorLinks(foreground, background){
    foreground = foreground || BLACK;
    background = background || WHITE;

    var links = document.getElementsByTagName("a");
    for (var i=0; i<links.length; i++){
            if(links[i].href){
                    links[i].style.color = foreground;
                    links[i].style.backgroundColor = background;
            }
    }

    coo.setCookie('fglink', foreground, 365)
    coo.setCookie('bglink', background, 365)
}


function randomColor(){
    return Color.rgb(
        parseInt(Math.random()*256),
        parseInt(Math.random()*256),
        parseInt(Math.random()*256)
        );
}

function randomHexColorPair(){
    const r = 4.5;

    var fore = randomColor();
    var back = randomColor();
    //console.log(fore.toString(), back.toString(), 'hex: ', fore.hex(), back.hex());

    //window.fore = fore;

    ratio=fore.contrast(back) ;
    while(ratio < r){
        back = randomColor();
        ratio=fore.contrast(back) ;

        //window.back = back;
        //console.log(fore.toString(), back.toString(), 'hex: ', fore.hex(), back.hex());
    }

    var fHex = typeof fore === 'string' ? fore:fore.hex();
    var bHex = typeof back === 'string' ? back:back.hex();

    return [fHex, bHex];
}


function randomBodyColor(){
    const r = 4.5;

    [fore, back] = randomHexColorPair();
    //console.log(fore.toString(), back.toString(), 'hex: ', fore.hex(), back.hex());
    console.log(fore.toString(), back.toString(), );

    bodyColor(fore, back);
}


function randomLinkColor(){
    const r = 4.5;

    [fore, back] = randomHexColorPair();
    //console.log(fore.toString(), back.toString(), 'hex: ', fore.hex(), back.hex());
    console.log('link color ', fore.toString(), back.toString(), );

    colorLinks(fore, back);
}


function rollBodyForeground(){
    var r = 4.5;

    //var fore = document.body.style.color;
    var back = document.body.style.backgroundColor;

    var f = randomColor(), b = Color(back);

    var ratio = f.contrast(b);
    console.log(`ratio < r ? ${ratio} < ${r}`);
    while(ratio < r){
        f = randomColor();
        ratio = f.contrast(b);
    }

    console.log(f.hex(), b.hex(), ratio);

    //document.body.style.color = f.hex();
    //document.body.style.backgroundColor = b.hex();
    bodyColor(f.hex(), b.hex());
}

function rollLinkForeground(){
    var r = 4.5;

    //var fore = document.body.style.color;
    var back = document.body.style.backgroundColor;

    var f = randomColor(), b = Color(back);

    var ratio = f.contrast(b);
    console.log(`ratio < r ? ${ratio} < ${r}`);
    while(ratio < r){
        f = randomColor();
        ratio = f.contrast(b);
    }

    console.log(f.hex(), b.hex(), ratio);

    //document.body.style.color = f.hex();
    //document.body.style.backgroundColor = b.hex();
    colorLinks(f.hex(), b.hex());
}

//document.getElementById('randombodycolor').onclick = randomBodyColor;
//document.getElementById('redoColor').onclick = redoColor;
//document.getElementById('rollBodyForeground').onclick = rollBodyForeground;


//window.randomHexColorPair = randomHexColorPair;
//window.randomColor = randomColor;
//window.randomBodyColor = randomBodyColor;


//colorDefault();

module.exports.bodyColor = bodyColor;
module.exports.randomBodyColor = randomBodyColor;
module.exports.colorLinks = colorLinks;
module.exports.randomLinkColor = randomLinkColor;
module.exports.rollLinkForeground = rollLinkForeground;
module.exports.rollBodyForeground = rollBodyForeground;
