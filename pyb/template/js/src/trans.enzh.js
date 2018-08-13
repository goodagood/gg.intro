
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
