
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
    fetch online file,
    cp folder file tree
    render to HTML


    """


    print("copy and set target : ", tgt)
    tool.copytree(mdsrc, tgt)

    # Instead of clone the repo, we get the single raw file from github
    Story_Path = os.path.join(tgt, os.path.basename(online_file))
    print( "fetch page: %s  --> %s"%(raw_git, Story_Path))
    fetch138.get_single_file(raw_git, Story_Path)

    template_components(template_path, tgt)

    print("make HTML %s with root: %s"%(tgt, htmlRoot))
    htmlize(tgt, htmlRoot)

    # cn index
    mkindex.dotemplate(
            mdsrc   =config_files.Cn_index_md, 
            tplsrc  =config_files.Index_template,
            dst     =config_files.Cn_index_dst, 
            htmlRoot=config_files.HTMLRoot,
            lang_tag=config_files.En_lang_switch)  # cn page get a en switch, vice versa

    # en index
    mkindex.dotemplate(
            mdsrc   =config_files.En_index_md, 
            tplsrc  =config_files.Index_template,
            dst     =config_files.En_index_dst, 
            htmlRoot=config_files.HTMLRoot,
            lang_tag=config_files.Cn_lang_switch)  # en page get a cn switch, vice versa



def htmlize(mdfolder, htmlRoot=None):
    for mdfile in tool.find_md(mdfolder):
        # add .html to the markdown file name
        mkmd.md2html_same_folder(mdfile, htmlRoot)


def template_components(template_path, tgt, js_src=None, js_tgt=None, style_src=None, style_tgt=None):
    #print("copy template components ", script_path, tgt)

    if not js_src:
        js_src = os.path.join(template_path, 'js/src/index.browserify.js')

    if not js_tgt:
        js_tgt = os.path.join(template_path, 'js/index.js')

    compile_js_css.prepare_js(js_src, js_tgt)

    if not style_src:
        style_src  = os.path.join(template_path, 'style/src/index.scss')
        pass
    if not style_tgt:
        style_tgt  = os.path.join(template_path, 'style/index.css')

    compile_js_css.prepare_css(style_src, style_tgt)
    compile_js_css.single_css()
    #mk_single_css();

    print("-- copy template components ", template_path, tgt)
    pre_template.copy_template_components(template_path, tgt)



if __name__ == "__main__":

    #MDFolder = os.path.expanduser("/tmp/md.files")
    MDFolder = os.path.expanduser("~/workspace/gg.intro/md.files")

    TemplateFolder = os.path.expanduser("~/workspace/gg.intro/template")

    script_src = os.path.join(TemplateFolder, 'js/src/index.js')
    script_tgt = os.path.join(TemplateFolder, 'js/index.js')

    style_src  = os.path.join(TemplateFolder, 'style/src/index.scss')
    style_tgt  = os.path.join(TemplateFolder, 'style/index.css')

    #HTMLFolder = "/tmp/aug11"  # as temperory default
    HTMLFolder = "/my/outside/aug22"  # as temperory default
    HTMLRoot   = "/aug22"

    raw_git = "https://raw.githubusercontent.com/goodagood/story/master/y10m/b.markdown"

    # hard coded ?
    #Story_Path = os.path.join(HTMLFolder, 'b.md')


    #test_do_all(mdsrc, template_path, tgt, online_file, htmlRoot=None):
    test_do_all(
            mdsrc         =config_files.MDFolder,
            template_path =config_files.Template_folder,
            tgt           =config_files.HTMLFolder,
            online_file   =config_files.Raw_git,
            htmlRoot      =config_files.HTMLRoot)

    #htmlize(HTMLFolder, htmlRoot=HTMLRoot)

    #template_components(HTMLFolder)

    #print(MDFolder, TemplateFolder, HTMLFolder, raw_git)
    #pre_template.copy_template_components(TemplateFolder, HTMLFolder)
    pass

