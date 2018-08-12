
const $ = require("jquery");

//const pcolor = require("../mycolor.js");
//const pcolor = require("page.color/mycolor.js");

const Color = require("./color.js");

const coo = require("./cookie.js");

const p = console.log;


document.getElementById('randomColor').onclick = function(e){
    if(e) e.preventDefault();
    Color.randomBodyColor();
    Color.rollLinkForeground();
};
document.getElementById('textColor').onclick = function(e){
    if(e) e.preventDefault();
    Color.rollBodyForeground();
};



$( document ).ready(function() {

    // retrieve color and set it,
    // retrieve cookies and do the settings

    var fgcolor = coo.getCookie('fpcolor');
    var bgcolor = coo.getCookie('bgcolor');
    var fglink  = coo.getCookie('fplink');
    var bglink  = coo.getCookie('bglink');

    var bodyFontSize  = coo.getCookie('bodyFontSize');

    if(fgcolor || bgcolor) Color.bodyColor(fgcolor, bgcolor); 
    if(fglink  || bglink ) Color.colorLinks(fglink, bglink); 
    if(bodyFontSize) document.body.style.fontSize = bodyFontSize;
    console.log('did we set it? ', fgcolor, bgcolor, fglink, bglink, bodyFontSize);

    //var width = $(window).width();
    //console.log('width', width);


    // do my translate 

    var dictionary = {
        en: {
            "login":  "LOGIN",
            "username":  "User Name",
            "password":  "Password",
            "i18key": "hello world",
            "testi18n": "TEST I18N"
        },

        zh: {
            "login":  "登录",
            "username":  "用户名",
            "password":  "密码",

            "i18key": "hello world",
            "testi18n": "测试 i18next "
        }
    };

    function trans(key, lang){
        if(!key) return null;
        if(!lang) return null;

        if(dictionary[lang]){
            if(dictionary[lang][key]) return dictionary[lang][key];
        }
        return null;
    }

    //$("#ptesti18n").html(trans("testi18n", 'zh'));

    var userLang = navigator.language || navigator.userLanguage;
    //console.log('userLang');
    //console.log(userLang);

    if(/zh/.test(userLang)){
        $(".ggtt").each(function(){
            //console.log($(this).html());
            //console.log($(this).data("ggtt"));
            //console.log( trans($(this).data("ggtt"), "zh"));

            var key = $(this).data("ggtt");
            if(key){
                var translated = trans(key, "zh");
                if(translated) $(this).html(translated);
            }
        });
    }

    //$(".ggtt").html(trans($(this).data("ggtt"), "zh"));


});



/*
 * Do body font size
 */
function getBodyFontSize(){
  var fs = document.body.style.fontSize;
  if (fs && fs !== ""){
    return fs;
  }
  return window.getComputedStyle(document.body).fontSize;
}

function increaseBodyFontSize(e){
  e.preventDefault();
  var size = getBodyFontSize();
  intSize  = parseInt(size);
  p(`size: ${size}, `);
  big = intSize + 1;
  
  value = `${big}px`;
  p(`size + 1: ${value}, `);

  document.body.style.fontSize = value;
  coo.setCookie("bodyFontSize", value, 365);
}

function decreaseBodyFontSize(e){
  e.preventDefault();
  var size = getBodyFontSize();
  intSize  = parseInt(size);
  p(`size: ${size}, `);
  small = intSize - 1;
  value = `${small}px`
  p(`size - 1: ${small}, `);
  //document.body.style.fontSize = `${small}px`;
  document.body.style.fontSize = value;
  coo.setCookie("bodyFontSize", value, 365);
}


var increaseEl = document.getElementById("increaseBodyFontSizeNavItem");
if (increaseEl.addEventListener){
    increaseEl.addEventListener("click", increaseBodyFontSize, false);
}else if (increaseEl.attachEvent){
    increaseEl.attachEvent('onclick', increaseBodyFontSize);
}

var decreaseEl = document.getElementById("decreaseBodyFontSizeNavItem");
if (decreaseEl.addEventListener){
    decreaseEl.addEventListener("click", decreaseBodyFontSize, false);
}else if (decreaseEl.attachEvent){
    decreaseEl.attachEvent('onclick', decreaseBodyFontSize);
}


//// switch the topnav to small icon, not used
//function w3topnavFun() {
//  var x = document.getElementById("w3topnav");
//  if (x.className === "topnav") {
//    x.className += " responsive";
//  } else {
//    x.className = "topnav";
//  }
//}
