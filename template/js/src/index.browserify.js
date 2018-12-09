
const $ = require("jquery");

//const pcolor = require("../mycolor.js");
//const pcolor = require("page.color/mycolor.js");

const Color = require("./color.js");

const cookie = require("./cookie.js");

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

	cookie.restorePresetCookies();

	//var width = $(window).width();
	//console.log('width', width);

	// do my translate 
	//$(".ggtt").html(trans($(this).data("ggtt"), "zh"));
	//$(".enzh").html(trans($(this).data("ggtt"), "zh"));
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
	cookie.setCookie("bodyFontSize", value, 365);
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
	cookie.setCookie("bodyFontSize", value, 365);
}


function changeBodyFontSize(delta){
	// delta is size in px to increase or decrease

	var size = getBodyFontSize();
	intSize  = parseInt(size);
	p(`old font size: ${size}, `);

	newSize = intSize + delta;
	value = `${newSize}px`
	p(`change font to: ${newSize}px`);

	document.body.style.fontSize = value;
	cookie.setCookie("bodyFontSize", value, 365);
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


