
# 
# Make single place to set files and folders used.
# 2018 0822
#

import os


# tilda means it's relative path to user HOME
MDFolder_tilda = "~/workspace/gg.intro/md.files"
MDFolder       = os.path.expanduser(MDFolder_tilda)

Template_folder = os.path.expanduser("~/workspace/gg.intro/template")
Template_file   = os.path.join(Template_folder, 'template.html')

Script_src = os.path.join(Template_folder, 'js/src/index.js')
Script_tgt = os.path.join(Template_folder, 'js/index.js')

Style_src  = os.path.join(Template_folder, 'style/src/index.scss')
Style_tgt  = os.path.join(Template_folder, 'style/index.css')

#HTMLFolder = "/tmp/aug11"  # as temperory default
HTMLFolder = "/my/outside/aug23"  # as temperory default
HTMLRoot   = "/aug23"

Raw_git = "https://raw.githubusercontent.com/goodagood/story/master/y10m/b.markdown"

# hard coded ?
#Story_Path = os.path.join(HTMLFolder, 'b.md')



#--- index en/cn

Index_template_tilde = '~/workspace/gg.intro/template/index.template.html'

Index_template = os.path.expanduser(Index_template_tilde)

#En_index_dst = os.path.expanduser('~/workspace/gg2/srv/public/index.html')
En_index_dst = os.path.join(HTMLFolder, 'index.html')

Cn_index_dst = os.path.join(HTMLFolder, 'index.cn.html')

#DST =   '/my/outside/md/index.html'


# ...

MD_Src_tilde = '~/workspace/gg.intro/md.files/intro.md'
MD_Src       = os.path.expanduser(MD_Src_tilde)

MD_Src_Cn_tilde = '~/workspace/gg.intro/md.files/cn/intro.md'
MD_Src_Cn       = os.path.expanduser(MD_Src_Cn_tilde)

Cn_lang_switch = """<a href="./index.cn.html" id="index-cn-link"> 中文 </a>"""
En_lang_switch = """<a href="./index.html" id="index-en-link"> English </a>"""


#CNDST = '/my/outside/md/index.cn.html'

#TMPDST =   '/tmp/index.html'
#TMPCNDST = '/tmp/index.cn.html'

#CNDST = '/tmp/index.cn.html'

#CNSRC = os.path.expanduser('~/workspace/gg.intro/md.files/cn/intro.md')
#CNDST = '/my/outside/md/index.cn.html'

#tmp = replace(SRC, DST)
#tmp = replace(CNSRC, CNDST)



