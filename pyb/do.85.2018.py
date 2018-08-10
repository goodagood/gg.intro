
import os
import subprocess


import tool
import pre_template
import fetch138

import compile_js_css
import mkmd
import mkindex


MDSrc = os.path.expanduser("~/workspace/gg.intro/md.files")

TGT_Folder = "/tmp/august10_1437pm"  # as temperory default

# hard coded
Story_Path = os.path.join(TGT_Folder, 'b.md')

#
# It should be clear to set all target now.
#

# copy file tree, clone online docs, prepare CSS JS, template,
# build html


def test_aug_10(src, tgt):


    tool.copytree(src, tgt)
    fetch138.hard_coded_story_clone(Story_Path)

    script_path = tool.find_script_path()
    pre_template.copy_template()


    for mdpath in tool.find_md(TGT_Folder):
        print(mdpath)

        # add .html to the markdown file name
        mkmd.md2html_same_folder(mdpath)


test_aug_10(MDSrc, TGT_Folder)
