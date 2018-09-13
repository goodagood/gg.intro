
import os
import sys
import subprocess


import tool
import pre_template
import fetch138

import compile_js_css
import mkmd
import mkindex

import config_files
import cmdargs


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
    #tool.copyfolder(template_path, tgt)
    template_tgt = os.path.join(tgt, os.path.basename(template_path))
    tool.copytree(template_path, template_tgt)


    # Instead of clone the repo, we get the single raw file from github
    Story_git = config_files.Story_git
    Story_Path = os.path.join(tgt, os.path.basename(online_file))
    print( "test do all> fetch page: %s  --> %s"%(Story_git, Story_Path))
    fetch138.get_single_file(Story_git, Story_Path)


    print("test do all> make HTML %s with root: %s"%(tgt, htmlRoot))
    htmlize(tgt, htmlRoot)

    do_index()
    pass


def do_index():
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



def do_selected(opt, mdsrc, template_path, tgt, online_file, htmlRoot=None):
    """ Do selected buildings, chose from opt, the rest same as "do all..."

    """

    if opt['copytree']:
        print("do selected> copy and set target : ", tgt)
        tool.copytree(mdsrc, tgt)

    if opt['template']:
        print("do selected> prepare_template_components(%s)"%template_path)
        print()
        prepare_template_components(template_path)

        template_tgt = os.path.join(tgt, os.path.basename(template_path))
        print('--template tgt ', template_tgt)

        # copy template folder as sub-folder into target
        # the components get used by html pages
        print("do selected> copy template components, tool.copyfolder(template_path, tgt)")
        print()
        tool.copytree(template_path, template_tgt) # this use copy tree


    if opt['story']:
        # Instead of clone the repo, we get the single raw file from github
        Story_git = config_files.Story_git
        Story_Path = os.path.join(tgt, os.path.basename(online_file))
        print( "do selected> fetch page: %s  --> %s"%(Story_git, Story_Path))
        print()
        fetch138.get_single_file(Story_git, Story_Path)


    if opt['html']:
        print("do selected> make HTML %s with root: %s"%(tgt, htmlRoot))
        print()
        htmlize(tgt, htmlRoot)

    if opt['index_files']:
        do_index()

    pass


def do_list_from_arguments():
    #print(cmdargs.get_args())
    parsed = cmdargs.get_args()
    print(1, parsed.wordlist)

    if not parsed.wordlist:
        print('no keywords given')
        return

    if len(parsed.wordlist) <1:
        print('zero keywords given')
        return

    opt = {
            'copytree':   False,
            'template':   False,
            'story':      False,
            'html':       False,
            'index_files':False
            }
    wlist = parsed.wordlist

    for key in parsed.wordlist:
        opt[key] = True

    #print('opt is: ', opt)

    do_selected(opt,
            mdsrc         =config_files.MDFolder,
            template_path =config_files.Template_folder,
            tgt           =config_files.HTMLFolder,
            online_file   =config_files.Raw_git,
            htmlRoot      =config_files.HTMLRoot)




if __name__ == "__main__":

    #test_do_all(
    #        mdsrc         =config_files.MDFolder,
    #        template_path =config_files.Template_folder,
    #        tgt           =config_files.HTMLFolder,
    #        online_file   =config_files.Raw_git,
    #        htmlRoot      =config_files.HTMLRoot)

    #htmlize(config_files.HTMLFolder, htmlRoot=config_files.HTMLRoot)

    #prepare_template_components(config_files.Template_folder)

    #print(MDFolder, Template_folder, HTMLFolder, raw_git)
    #pre_template.copy_template_components(Template_folder, HTMLFolder)


    #OPT = {
    #        'copytree': True,
    #        'template': True,
    #        'story':    True,
    #        'html':     True,
    #        'index_files':False
    #        }

    #do_selected(OPT,
    #        mdsrc         =config_files.MDFolder,
    #        template_path =config_files.Template_folder,
    #        tgt           =config_files.HTMLFolder,
    #        online_file   =config_files.Raw_git,
    #        htmlRoot      =config_files.HTMLRoot)



    #import cmdargs
    ##print(cmdargs.get_args())
    #parsed = cmdargs.get_args()
    #print(parsed.wordlist)

    #if not parsed.wordlist:
    #    print('no keywords given')
    #    sys.exit()

    #if parsed.wordlist:
    #    print(len(parsed.wordlist))

    #if len(parsed.wordlist) <1:
    #    print('zero keywords given')
    #    sys.exit()

    #opt = {
    #        'copytree':   False,
    #        'template':   False,
    #        'story':      False,
    #        'html':       False,
    #        'index_files':False
    #        }
    #wlist = parsed.wordlist

    #for key in parsed.wordlist:
    #    opt[key] = True

    #print('opt is: ', opt)

    #do_selected(opt,
    #        mdsrc         =config_files.MDFolder,
    #        template_path =config_files.Template_folder,
    #        tgt           =config_files.HTMLFolder,
    #        online_file   =config_files.Raw_git,
    #        htmlRoot      =config_files.HTMLRoot)

    do_list_from_arguments()
    pass

