
import os
import shutil

import mkmd
import tool


#print(type(mkmd.render_html))


#mkmd.render_html('/tmp/some',  '/tmp/b.html')

#mkmd.md2html_same_folder ('/tmp/some')



template = './template/template.html'

#src = "/tmp/story/y10m/b.markdown"
#tgt = "/my/outside/tmp/tmp.html"

script_path = tool.find_script_path()
print("sp script path: ", script_path)

template_path = os.path.join(script_path, template)
template_abs = os.path.abspath(template_path)
print("template abs p: ", os.path.abspath(template_abs))

#mkmd.mkhtml(template=template_abs, src=src, dst=tgt)



#src_folder = "/home/za/workspace/gg.intro/md.files"
src_folder = "/tmp/md.files"
tgt_folder = "/tmp/mdhtml"


# old way
#result_folder = "/tmp/mdhtml/md.files"


import shlex
import subprocess

tool.copytree(src_folder, tgt_folder)




import glob
def copy_template():
    js_path = os.path.join(script_path, 'template/js')
    js_files = os.path.join(script_path, 'template/js/*.js')
    style_path = os.path.join(script_path, 'template/style')
    style_files = os.path.join(script_path, 'template/style/*.css')

    #target

    for f in glob.glob(js_files):
        # copy is function copy f to target file or into the folder
        shutil.copy(f, tgt_folder)

    for f in glob.glob(style_files):
        # copy is function copy f to target file or into the folder
        shutil.copy(f, tgt_folder)


copy_template()


for mdpath in tool.find_md(tgt_folder):
    print(mdpath)

    # add .html to the markdown file name
    mkmd.md2html_same_folder(mdpath)



## re arranges, 2018 0810


