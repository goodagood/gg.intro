
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


def test_do_all(src, tgt, online_file, htmlRoot=None):
    """ Do all buildings.
    
    Compile template components, js, css
    fetch online file, 
    cp folder file tree
    render to HTML
    
    """


    print("copy and set target : ", tgt)
    tool.copytree(src, tgt)

    # Instead of clone the repo, we get the single raw file from github
    Story_Path = os.path.join(tgt, os.path.basename(online_file))
    print( "fetch page: %s  --> %s"%(raw_git, Story_Path))
    fetch138.get_single_file(raw_git, Story_Path)

    compile_js_css.prepare_css()
    compile_js_css.prepare_js()
    script_path = tool.find_script_path()

    print("copy template components ", script_path, tgt)
    pre_template.copy_template(script_path, tgt)

    print("make HTML %s with root: %s"%(tgt, htmlRoot))
    htmlize(tgt, htmlRoot)




def htmlize(mdfolder, htmlRoot=None):
    for mdfile in tool.find_md(mdfolder):
        # add .html to the markdown file name
        mkmd.md2html_same_folder(mdfile, htmlRoot)


def template_components(tgt):
    compile_js_css.prepare_css()
    compile_js_css.prepare_js()
    script_path = tool.find_script_path()

    print("copy template components ", script_path, tgt)
    pre_template.copy_template(script_path, tgt)



if __name__ == "__main__":

    MDFolder = os.path.expanduser("~/workspace/gg.intro/md.files")
    #MDFolder = os.path.expanduser("/tmp/md.files")


    #HTMLFolder = "/tmp/august10_1437pm"  # as temperory default
    #HTMLFolder = "/tmp/aug11"  # as temperory default

    HTMLFolder = "/my/outside/aug12"  # as temperory default

    raw_git = "https://raw.githubusercontent.com/goodagood/story/master/y10m/b.markdown"

    # hard coded
    Story_Path = os.path.join(HTMLFolder, 'b.md')


    #test_do_all(MDFolder, HTMLFolder, raw_git, '/aug12')

    #htmlize(HTMLFolder, htmlRoot='/aug12')

    template_components(HTMLFolder)
    pass

