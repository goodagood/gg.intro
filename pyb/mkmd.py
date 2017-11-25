
import os
import shutil
import markdown

import sys
sys.path.append('../py')
import mdfile


import tool



def mkmd(src, dst=None):
    """Make HTML from markdown source file, return str if no dst.
    """
    with open(src, 'r', encoding='utf-8') as f:
        fstr = f.read()

    html = markdown.markdown(fstr)
    if dst == None:
        return html

    with open(dst, 'w') as f:
        f.write(html)

    return html


# template things
import pystache

# render a md file to html
def render_html(src=None, dst=None):

    #if src == None:
    #    src = '/tmp/b.md'

    s = mkmd(src=src)

    #template ? path
    with open('./config/template.html', 'r') as t:
        temp = t.read()
        r = pystache.render(temp, {'html4markdown': s, 'htmlRoot': '/md'});

    with open(dst, 'w') as f:
        f.write(r)


def md2html_same_folder(src):
    #name = os.path.basename(src)
    #result_folder = os.path.join(param.target_dir, name)
    tgt = src + '.html'
    print('same dir', src, tgt)
    render_html(src, tgt)


import mdfile2folder
def md2index_same_folder(src):
    #name = os.path.basename(src)
    #result_folder = os.path.join(param.target_dir, name)

    #tgt = src + '.html'
    tgt = mdfile2folder.md_index_html(src)

    print('same dir index html folder', src, tgt)
    render_html(src, tgt)


def readTemplate():

    with open('./config/template.html', 'r', encoding='utf-8') as t:
        temp = t.read()
        return temp


def do_md_folder():
    """Transfer markdown files to html, parameter get from command line.
    """

    # source/target dir get from command line parameter -s -t
    param = tool.check_parameter()
    if not param.source_dir:
        print('not source dir')
        return
    print('>source dir', param.source_dir)
    print('>target dir', param.target_dir)

    if param.delete_dir:
        shutil.rmtree(param.target_dir)
        print('rm target dir', param.target_dir)

    # Copy the whole folder to target position
    tool.copyfolder(param.source_dir, param.target_dir)

    # get the path of the new folder, it's content just been copied in.
    name = os.path.basename(param.source_dir)
    result_folder = os.path.join(param.target_dir, name)
    print('result dir', result_folder)

    # find markdown files and do it
    for mdpath in tool.find_md(result_folder):
        print(mdpath)

        # add .html to the markdown file name
        md2html_same_folder(mdpath)

        # make a folder and build markdown as folder/index.html
        #md2index_same_folder(mdpath)





if __name__ == "__main__":
    src = "/home/za/workspace/gg.intro/md.files"
    dst = "/home/za/workspace/gg.intro/py.pelican/content"

    src = "/home/za/workspace/gg.intro/md.files"
    dst = "/my/outside/md/"


    Path = '/home/za/workspace/gg.intro/md.files/intro.md'
    CNPath = '/home/za/workspace/gg.intro/md.files/cn/intro.md'

    ##mkmd(src='/tmp/b.md', dst='/tmp/bcn.html')
    #s = mkmd(src='/tmp/b.md', dst=None)
    #t = readTemplate()
    #pystache.parse(t)

    #r = pystache.render('hi, {{who}}', {'who': 'some one'});
    #print(r)

    #render_html('/tmp/b.md', '/tmp/tgt/t.html')
    #render_html('/tmp/i.md', '/tmp/tgt/i.html')

    do_md_folder()
