
# 
# Make single place to set files and folders used.
# 2018 0822
# 
# In building, we need target folder prepared first for md, html, template
# components
# 2018 0906
#

import os


# This is target
HTMLFolder = "/my/outside/sept"  # as temperory default
HTMLRoot   = "/sept" # root for URLs

# tilda means it's relative path to user HOME
MDFolder_tilda = "~/workspace/gg.intro/md.files"
MDFolder       = os.path.expanduser(MDFolder_tilda)

Template_folder = os.path.expanduser("~/workspace/gg.intro/template")
Template_file   = os.path.join(Template_folder, 'template.html')

### move compiled template components outside
template_name = os.path.basename(Template_folder)
Template_target = os.path.join(HTMLFolder, template_name)


Script_src = os.path.join(Template_folder, 'js/src/index.js')

#Script_tgt = os.path.join(Template_folder, 'js/index.js')
Script_tgt = os.path.join(Template_target, 'js/index.js')

Style_src  = os.path.join(Template_folder, 'style/src/index.scss')
# use more specific name:
Style_scss  = os.path.join(Template_folder, 'style/src/index.scss')

#Style_tgt  = os.path.join(Template_folder, 'style/index.css')
Style_tgt  = os.path.join(Template_target, 'style/index.css')


Raw_git = "https://raw.githubusercontent.com/goodagood/story/master/y10m/b.markdown"
Story_git = "https://raw.githubusercontent.com/goodagood/story/master/y10m/b.markdown"

#Story_Path = os.path.join(HTMLFolder, 'b.md')



#--- index en/cn

Index_template_tilde = os.path.join(Template_folder, 'index.template.html')
Index_template       = os.path.expanduser(Index_template_tilde)

En_index_dst = os.path.join(HTMLFolder, 'index.html')

Cn_index_dst = os.path.join(HTMLFolder, 'index.cn.html')


# If we build Single CSS and JS

JS_src_folder = "js/src"
JS_file = "index.browserify.js"
#JS_src = '~/workspace/gg.intro/template/js/src/index.browserify.js'
JS_src = os.path.join(Template_folder, JS_src_folder, JS_file)

# target is the target of template building phase
JS_tgt = os.path.join(Template_folder, 'js/bundle.js')
CSS_tgt = os.path.join(Template_folder, 'style/bundle.js')


CSS = "bundle.css"
JS  = "bundle.js"
CSS_dst = os.path.join(HTMLFolder, CSS)
JS_dst  = os.path.join(HTMLFolder, JS)

# If we build index.html file
Index_CSS = "index.bundle.css"
Index_JS  = "index.bundle.js"
Index_CSS_dst = os.path.join(HTMLFolder, CSS)
Index_JS_dst  = os.path.join(HTMLFolder, JS)


###

En_index_md_tilde = '~/workspace/gg.intro/md.files/intro.md'
En_index_md       = os.path.expanduser(En_index_md_tilde)

Cn_index_md_tilde = '~/workspace/gg.intro/md.files/cn/intro.md'
Cn_index_md       = os.path.expanduser(Cn_index_md_tilde)

Cn_lang_switch = """<a href="./index.cn.html" id="index-cn-link"> 中文 </a>"""
En_lang_switch = """<a href="./index.html" id="index-en-link"> English </a>"""





if __name__ == "__main__":
    #print(JS_src, JS_dst)
    print(template_name)
    print(Template_target)
    print(Script_tgt)
    print(Style_tgt)
