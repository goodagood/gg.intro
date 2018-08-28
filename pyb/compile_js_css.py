
import os
import subprocess
import shlex

import config_files as Config



#d
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
    """js folders can be hard-coded, It happens only in template.
    """

    # New location of the js index, 2018 0806
    if not src:
        #src = '~/workspace/gg.intro/template/js/src/index.browserify.js'
        src = Config.JS_src
        pass
    js_input = os.path.expanduser(src)


    # new location
    if not tgt:
        #tgt = '~/workspace/gg.intro/template/js/bundle.js'
        tgt = Config.JS_tgt
        pass
    js_target = os.path.expanduser(tgt)

    #print(js_input, js_target)
    return browserify_js(js_input, js_target)



def browserify_js(src, tgt, cwd=None):
    """I have to write commands in one line and use subprocess.call

    Should return shell return code
    """
    if not cwd:
        cwd=os.path.expanduser(Config.Template_folder)

    # cmdj = """browserify %s --debug -o  %s """%(src, tgt)
    cmdj = """npx browserify %s --debug -o  %s """%(src, tgt)
    print("command line:> %s"%cmdj)
    
    #subprocess.call(cmdj, shell=True)
    #return cmdj

    cmd_args = shlex.split(cmdj)
    #return subprocess.check_output(cmd_args) #can't set shell?: shell=True
    return subprocess.Popen(cmd_args, cwd=cwd)


#d
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
# redo from 'compile_css', normalize it. 2018 0808
#
def prepare_css(src=None, tgt=None):
    """edit from compile css, upgrade to seperate file name
    """

    if not src:
        # the file moved
        #src = '~/workspace/gg.intro/pyb/template/style/src/index.scss'
        src = Config.Style_scss
    css_src = os.path.expanduser(src)

    # new location
    if not tgt:
        #tgt = '~/workspace/gg.intro/pyb/template/style/index.css'
        tgt = Config.Style_tgt
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



def single_css(tgt=None):
    """make a single CSS file.

    Most names and path would be hard-wired.
    It's node.js doing the job, tested, not ready
    """
    cmd_single_css = "node clean.css.js"
    args_of_cmd = shlex.split(cmd_single_css)
    wdir = os.path.abspath("../template")
    #subprocess.call(cmd_single_css, shell=True)
    print(wdir, args_of_cmd)
    p = subprocess.Popen(args_of_cmd, cwd=wdir)
    print('single css subprocess Popen return ', p)
    return p


def both():
    compile_css()
    compile_js()



if __name__ == "__main__":

    #what = compile_css()
    #print(what)


    #both()

    #prepare_css()
    out = prepare_js()
    print(out)

    #single_css()
    pass
