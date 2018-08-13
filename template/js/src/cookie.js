


function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


function getCookie(cname, defaults) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }

    if(defaults){ 
            return defaults;
    }else{
            return '';
    }
}


//?
function checkCookie() {
    var user = getCookie("username");
    if (user != "") {
        alert("Welcome again " + user);
    } else {
        user = prompt("Please enter your name:", "");
        if (user != "" && user != null) {
            setCookie("username", user, 365);
        }
    }
} 


let Color = require('./color.js');

function restorePresetCookies(){
    var fgcolor = getCookie('fpcolor', 'BALCK');
    var bgcolor = getCookie('bgcolor', 'WHITE');
    var fglink  = getCookie('fplink',  'BALCK');
    var bglink  = getCookie('bglink',  'WHITE');

    var bodyFontSize  = getCookie('bodyFontSize', '18px');

    if(fgcolor || bgcolor) Color.bodyColor(fgcolor, bgcolor); 
    if(fglink  || bglink)  Color.colorLinks(fglink, bglink); 

    if(bodyFontSize) document.body.style.fontSize = bodyFontSize;
}


module.exports.getCookie = getCookie;
module.exports.setCookie = setCookie;
module.exports.restorePresetCookies = restorePresetCookies;

// for testing
module.exports.checkCookie = checkCookie;
