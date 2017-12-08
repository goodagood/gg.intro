
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



def both():
    compile_css()
    compile_js()


if __name__ == "__main__":

    #jscmd = compile_js()
    #js1a = jscmd[0].split()

    what = compile_css()

    #both()
