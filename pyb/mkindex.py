
# make index.html and index.cn.html from markdown contents
#
# Using mustache template python version pystache.
# In the html template if there are un-satisfied variables,
# it will raise exception.
#
# markdown, template, files are hardwired.


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



def replace(mdsrc=None, tplsrc=None, dst=None):
    """do with string replacing

    Change to using mustache/pystache template.
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
    #print(mdsrc, tplsrc, dst, htmlRoot)

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



if __name__ == "__main__":

    index_template = os.path.expanduser(
            '~/workspace/gg2/srv/public/index.template.html')

    index_dst = os.path.expanduser('~/workspace/gg2/srv/public/index.html')
    cnindex_dst = os.path.expanduser('~/workspace/gg2/srv/public/index.cn.html')

    SRC = '/home/za/workspace/gg.intro/md.files/intro.md'
    SRC = os.path.expanduser(SRC)
    DST =   '/my/outside/md/index.html'

    TMPDST =   '/tmp/index.html'
    TMPCNDST = '/tmp/index.cn.html'
    #CNDST = '/tmp/index.cn.html'

    CNSRC = os.path.expanduser('~/workspace/gg.intro/md.files/cn/intro.md')
    CNDST = '/my/outside/md/index.cn.html'

    #tmp = replace(SRC, DST)
    #tmp = replace(CNSRC, CNDST)


    cn_lang_switch = """<a href="./index.cn.html" id="index-cn-link"> 中文 </a>"""
    en_lang_switch = """<a href="./index.html" id="index-en-link"> English </a>"""


    print("""Do index
    md src\t: %s,
    template\t: %s,
    destination\t: %s
    \r\n"""%(
        SRC, index_template, DST))

    dotemplate(SRC, index_template, DST, '/md', lang_tag=cn_lang_switch)

    print("""Do cn index
    md src\t: %s,
    template\t: %s,
    destination\t: %s """%(
        CNSRC, index_template, CNDST))

    dotemplate(mdsrc=CNSRC, tplsrc=index_template, dst=CNDST,
            htmlRoot='/md', lang_tag=en_lang_switch)


