
import os
import subprocess

#import time
#time.sleep(5)


def compile_js():
    """I have to write commands in one line and use subprocess.call
    """

    jsinput = '~/workspace/gg.intro/pyb/config/prepare/index.js'
    jsinput = os.path.expanduser(jsinput)

    js_target =  "~/workspace/gg.intro/pyb/config/bundle.js"
    js_target = os.path.expanduser(js_target)

    js_gg2 =  "~/workspace/gg2/srv/public/bundle.js"
    js_gg2 = os.path.expanduser(js_gg2)

    cmdj = """browserify %s --debug -o  /my/outside/md/bundle.js """%jsinput
    print(cmdj)

    # copy back
    cpj = """cp  /my/outside/md/bundle.js  %s  """%js_target
    # copy to gg2/srv/public
    cpjgg2 = """cp  /my/outside/md/bundle.js %s """%js_gg2


    subprocess.call(cmdj, shell=True)
    subprocess.call(cpj, shell=True)
    subprocess.call(cpjgg2, shell=True)

    return [cmdj, cpj, cpjgg2]


#  
# Make it easy to set source and target, same as compile_js.
# 2018 0806
#

def prepare_js(src=None, tgt=None):
    #def js_folders(src, tgt):
    """js folders can be hard-coded, It happens only in template.
    """

    #jsinput = '~/workspace/gg.intro/pyb/config/prepare/index.js'
    #jsinput = os.path.expanduser(jsinput)
    #
    # New location of the js index, 2018 0806
    if not src:
        src = '~/workspace/gg.intro/pyb/template/js/src/index.browserify.js'
        pass
    js_input = os.path.expanduser(src)


    #js_target =  "~/workspace/gg.intro/pyb/config/bundle.js"
    #js_target = os.path.expanduser(js_target)
    #
    # new location
    if not tgt:
        tgt = '~/workspace/gg.intro/pyb/template/js/index.js'
        pass
    js_target = os.path.expanduser(tgt)


    #print(js_input, js_target)
    browserify_js(js_input, js_target)



def browserify_js(src, tgt):


    """I have to write commands in one line and use subprocess.call
    """


    #redoing
    # cmdj = """browserify %s --debug -o  %s """%(src, tgt)
    cmdj = """npx browserify %s --debug -o  %s """%(src, tgt)
    print(cmdj)
    subprocess.call(cmdj, shell=True)

    ## copy back
    #cpj = """cp  /my/outside/md/bundle.js  %s  """%js_target
    ## copy to gg2/srv/public
    #cpjgg2 = """cp  /my/outside/md/bundle.js %s """%js_gg2


    #subprocess.call(cmdj, shell=True)
    #subprocess.call(cpj, shell=True)
    #subprocess.call(cpjgg2, shell=True)

    #return [cmdj, cpj, cpjgg2]





def compile_css():
    """I have to write commands in one line and use subprocess.call
    """

    css_src = '~/workspace/gg.intro/pyb/config/prepare/index.scss'
    css_src = os.path.expanduser(css_src)

    css_target = '~/workspace/gg.intro/pyb/config/styles/index.css'
    css_target = os.path.expanduser(css_target)

    css_map_target = '~/workspace/gg.intro/pyb/config/styles/'
    css_map_target = os.path.expanduser(css_map_target)

    gg2css_target = '~/workspace/gg2/srv/public/stylesheets/index.css'
    gg2css_target = os.path.expanduser(gg2css_target)

    gg2css_map_target = '~/workspace/gg2/srv/public/stylesheets/'
    gg2css_map_target = os.path.expanduser(gg2css_map_target)

    cmdcss = """scss %s  /my/outside/md/styles/index.css   """%css_src


    # copy back
    cpc = """cp  /my/outside/md/styles/index.css  %s """%css_target
    cpcssmap = """cp /my/outside/md/styles/index.css.map   %s """%css_map_target

    # copy to gg2/srv/public
    cpc2gg2 = """cp  /my/outside/md/styles/index.css  %s """%gg2css_target
    cpcssmap2gg2 = """cp  /my/outside/md/styles/index.css.map %s
    """%gg2css_map_target



    # start to run commands

    print (cmdcss)
    subprocess.call(cmdcss, shell=True)

    print (cpc)
    subprocess.call(cpc, shell=True)
    print (cpcssmap)
    subprocess.call(cpcssmap, shell=True)
    print (cpc2gg2)
    subprocess.call(cpc2gg2, shell=True)
    print (cpcssmap2gg2)
    subprocess.call(cpcssmap2gg2, shell=True)

    return {"css_src": css_src,
            "css_target": css_target,
            "css_map_target": css_map_target,
            "gg2css_target": css_target,
            "gg2css_map_target": css_map_target,
            "cmdcss": cmdcss,
            "cpc": cpc,
            "cpcssmap": cpcssmap,
            "cpc2gg2": cpc2gg2,
            "cpcssmap2gg2": cpcssmap2gg2,
            }


#
# start from compile_css, normalize it. 2018 0808
#

def prepare_css(src=None, tgt=None):
    """edit from compile css, upgrade to seperate file name
    """

    if not src:
        # the file moved
        src = '~/workspace/gg.intro/pyb/template/style/src/index.scss'
    css_src = os.path.expanduser(src)

    # new location
    if not tgt:
        tgt = '~/workspace/gg.intro/pyb/template/style/index.css'
    css_target = os.path.expanduser(tgt)

    cmdcss = """sass %s  %s  """%(css_src, css_target)



    # start to run commands

    print (cmdcss)
    subprocess.call(cmdcss, shell=True)


    return {"css_src": css_src,
            "css_target": css_target,
            "cmdcss": cmdcss,
            }

    pass



def single_css(tgt):
    """make a single CSS file.

    Most names and path would be hard-wired.
    It's node.js doing the job, tested, not ready
    """
    cmd_single_css = "node single_css"
    subprocess.call(cmd_single_css, shell=True)
    pass


def both():
    compile_css()
    compile_js()


if __name__ == "__main__":

    #what = compile_css()
    #print(what)

    
    #both()

    prepare_css()
    #prepare_js()
    pass
