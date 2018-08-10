
import os

import mkmd
import tool

print(type(mkmd.render_html))


#mkmd.render_html('/tmp/some',  '/tmp/b.html')

#mkmd.md2html_same_folder ('/tmp/some')



template = './template/template.html'

src = "/tmp/story/y10m/b.markdown"
tgt = "/my/outside/tmp/tmp.html"

sp = tool.find_script_path()
print("sp script path: ", sp)

template_abs = os.path.join(sp, template)

#mkmd.mkhtml(template=template_abs, src=src, dst=tgt)



src_folder = "/home/za/workspace/gg.intro/md.files"
src_folder = "/tmp/md.files"
tgt_folder = "/tmp/mdhtml"

result_folder = "/tmp/mdhtml/md.files"


## prepare
import shlex
import subprocess

tool.copyfolder(src_folder, tgt_folder)
## end of prepare


for mdpath in tool.find_md(result_folder):
    print(mdpath)

    # add .html to the markdown file name
    #md2html_same_folder(mdpath)



