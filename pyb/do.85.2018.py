
import os
import subprocess


import tool
import pre_template
import fetch138

import compile_js_css
import mkmd
import mkindex

import config_files


#
# It should be clear to set all target now.
#

# copy file tree, clone online docs, prepare CSS JS, template,
# build html


def test_do_all(mdsrc, template_path, tgt, online_file, htmlRoot=None):
    """ Do all buildings, we hardwired many path

    Compile template components, js, css
        'template_path' is original path of template folder
    fetch online file,
    cp folder file tree
    render to HTML
    """

    print("test do all> prepare_template_components(%s)"%template_path)
    prepare_template_components(template_path)
    # prepare template components for index pages, or other categories

    print("test do all> copy and set target : ", tgt)
    tool.copytree(mdsrc, tgt)

    # copy template folder as sub-folder into target
    # the components get used by html pages
    print("test do all> tool.copyfolder(template_path, tgt)")
    tool.copyfolder(template_path, tgt)

    # Instead of clone the repo, we get the single raw file from github
    Story_git = config_files.Story_git
    Story_Path = os.path.join(tgt, os.path.basename(online_file))
    print( "test do all> fetch page: %s  --> %s"%(Story_git, Story_Path))
    fetch138.get_single_file(Story_git, Story_Path)


    print("test do all> make HTML %s with root: %s"%(tgt, htmlRoot))
    htmlize(tgt, htmlRoot)

    # If we want to build index(.cn).html differently
    # cn index
    #c name
    mkindex.index_get_template(
            mdsrc   =config_files.Cn_index_md, 
            tplsrc  =config_files.Index_template,
            dst     =config_files.Cn_index_dst, 
            htmlRoot=config_files.HTMLRoot,
            lang_tag=config_files.En_lang_switch)  # cn page get a en switch, vice versa

    # en index
    mkindex.index_get_template(
            mdsrc   =config_files.En_index_md, 
            tplsrc  =config_files.Index_template,
            dst     =config_files.En_index_dst, 
            htmlRoot=config_files.HTMLRoot,
            lang_tag=config_files.Cn_lang_switch)  # en page get a cn switch, vice versa



def htmlize(mdfolder, htmlRoot=None):
    for mdfile in tool.find_md(mdfolder):
        # add .html to the markdown file name
        mkmd.md2html_same_folder(mdfile, htmlRoot)


def prepare_template_components(template_folder, js_src=None, js_tgt=None, style_src=None, style_tgt=None):

    if not js_src:
        js_src = os.path.join(template_folder, 'js/src/index.browserify.js')

    if not js_tgt:
        js_tgt = os.path.join(template_folder, 'js/bundle.js')

    #js
    #print("compile_js_css.prepare_js({js_src}, {js_tgt})".format(js_src=js_src, js_tgt=js_tgt))
    compile_js_css.prepare_js(js_src, js_tgt)

    if not style_src:
        style_src  = os.path.join(template_folder, 'style/src/index.scss')
        pass
    if not style_tgt:
        style_tgt  = os.path.join(template_folder, 'style/bundle.css')

    #css
    compile_js_css.prepare_css(style_src, style_tgt)
    compile_js_css.single_css()



if __name__ == "__main__":

    #MDFolder = os.path.expanduser("~/workspace/gg.intro/md.files")

    #Template_folder = os.path.expanduser("~/workspace/gg.intro/template")

    #script_src = os.path.join(Template_folder, 'js/src/index.js')
    #script_tgt = os.path.join(Template_folder, 'js/index.js')

    #style_src  = os.path.join(Template_folder, 'style/src/index.scss')
    #style_tgt  = os.path.join(Template_folder, 'style/index.css')

    ##HTMLFolder = "/tmp/aug11"  # as temperory default
    #HTMLFolder = "/my/outside/aug22"  # as temperory default
    #HTMLRoot   = "/aug22"

    #raw_git = "https://raw.githubusercontent.com/goodagood/story/master/y10m/b.markdown"

    # hard coded ?
    #Story_Path = os.path.join(HTMLFolder, 'b.md')


    #test_do_all(mdsrc, template_path, tgt, online_file, htmlRoot=None):
    test_do_all(
            mdsrc         =config_files.MDFolder,
            template_path =config_files.Template_folder,
            tgt           =config_files.HTMLFolder,
            online_file   =config_files.Raw_git,
            htmlRoot      =config_files.HTMLRoot)

    #htmlize(config_files.HTMLFolder, htmlRoot=config_files.HTMLRoot)

    #prepare_template_components(config_files.Template_folder)

    #print(MDFolder, Template_folder, HTMLFolder, raw_git)
    #pre_template.copy_template_components(Template_folder, HTMLFolder)
    pass

