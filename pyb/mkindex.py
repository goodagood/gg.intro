
# make index.html and index.cn.html from markdown contents
#
# Using mustache template python version pystache.
# In the html template if there are un-satisfied variables,
# it will raise exception.


import os

import pystache

import mkmd


tmpstr ='''
    intro begin -->
  <div id="intro">

    ...

    intro end

'''

extra_head = """
  <!--intro begin-->

"""
# tail is not necessary
extra_tail = """
  <!--intro end-->

"""

SRC = '/home/za/workspace/gg.intro/md.files/intro.md'
DST = '/tmp/index.html'

CNSRC = '/home/za/workspace/gg.intro/md.files/cn/intro.md'
CNDST = '/tmp/index.cn.html'


def replace(mdsrc=None, tplsrc=None, dst=None):
    """
    """

    #src = '/home/za/workspace/gg.intro/md.files/intro.md'
    #dst = '/tmp/index.html'

    s = mkmd.mkmd(mdsrc)
    s = extra_head + s

    # target
    index   = os.path.expanduser('~/workspace/gg2/srv/public/index.html')
    cnindex = os.path.expanduser('~/workspace/gg2/srv/public/index.cn.html')
    print(index, cnindex)

    #index
    with open(index, 'r') as t:
        temp = t.read()

        start = temp.find('<!--intro begin-->')
        end = temp.find('<!--intro end-->')

        head = temp[:start]
        tail = temp[end:]
        all  = head + s + tail

    with open(dst, 'w') as f:
        f.write(all)

    return all


def dotemplate(mdsrc=None, tplsrc=None, dst=None, htmlRoot='', lang_tag=None):
    print(mdsrc, tplsrc, dst, htmlRoot)
    s = mkmd.mkmd(src=mdsrc)

    with open(tplsrc, 'r') as t:
        template = t.read()
        pass

    #return template #indev

    result = pystache.render(template, {
        'html4markdown': s,
        'htmlRoot': htmlRoot,
        'langswitch':lang_tag})

    with open(dst, 'w') as f:
        f.write(result)

    pass


if __name__ == "__main__":

    index_template = os.path.expanduser(
            '~/workspace/gg2/srv/public/index.template.html')
    index = os.path.expanduser('~/workspace/gg2/srv/public/index.html')
    cnindex = os.path.expanduser('~/workspace/gg2/srv/public/index.cn.html')

    #tmp = replace(SRC, DST)
    #tmp = replace(CNSRC, CNDST)


    cn_lang_switch = """<a href="./index.cn.html" id="index-cn-link"> 中文 </a>"""
    en_lang_switch = """<a href="./index.html" id="index-en-link"> English </a>"""

    dotemplate(SRC, index_template, index, '/md', lang_tag=cn_lang_switch)
    dotemplate(mdsrc=CNSRC, tplsrc=index_template, dst=cnindex,
            htmlRoot='/md', lang_tag=en_lang_switch)

