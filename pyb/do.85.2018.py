
import os
import subprocess


import tool
import pre_template
import fetch138

import compile_js_css
import mkmd
import mkindex



#
# It should be clear to set all target now.
#

# copy file tree, clone online docs, prepare CSS JS, template,
# build html

raw_git = "https://raw.githubusercontent.com/goodagood/story/master/y10m/b.markdown"

def test_aug_10(src, tgt):
    """
    
    The local story is b.md, we get online
    """


    tool.copytree(src, tgt)

    #fetch138.hard_coded_story_clone(Story_Path)
    # Instead of clone the repo, we get the raw file from github
    Story_Path = os.path.join(tgt, 'b.md')
    print( "fetch page: %s  --> %s"%(raw_git, Story_Path))
    fetch138.get_single_file(raw_git, Story_Path)

    script_path = tool.find_script_path()
    print("copy template components ", script_path, tgt)
    pre_template.copy_template(script_path, tgt)


    print("make HTML")
    htmlize(TGT_Folder)
    #for mdpath in tool.find_md(TGT_Folder):
    #    print(mdpath)

    #    # add .html to the markdown file name
    #    #mkmd.md2html_same_folder(mdpath)




def htmlize(mdfolder):
    for mdfile in tool.find_md(mdfolder):
        print(mdfile)

        # add .html to the markdown file name
        mkmd.md2html_same_folder(mdfile)





if __name__ == "__main__":

    MDSrc = os.path.expanduser("~/workspace/gg.intro/md.files")
    #MDSrc = os.path.expanduser("/tmp/md.files")


    #TGT_Folder = "/tmp/august10_1437pm"  # as temperory default
    #TGT_Folder = "/tmp/aug11"  # as temperory default
    TGT_Folder = "/my/outside/aug11"  # as temperory default

    # hard coded
    Story_Path = os.path.join(TGT_Folder, 'b.md')



    test_aug_10(MDSrc, TGT_Folder)

    pass

