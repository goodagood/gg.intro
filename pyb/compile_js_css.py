
import subprocess


def compile_js_css():
    """I have to write commands in one line and use subprocess.call
    """

    cmdj = """browserify ~/workspace/gg.intro/pyb/config/prepare/index.js   --debug -o  /my/outside/md/bundle.js """
    print(cmdj.split())

    # copy back
    cpj = """cp  /my/outside/md/bundle.js ~/workspace/gg.intro/pyb/config/bundle.js   """
    # copy to gg2/srv/public
    cpjgg2 = """cp  /my/outside/md/bundle.js ~/workspace/gg2/srv/public/bundle.js   """


    #cmdcss = """scss ~/workspace/gg.intro/pyb/config/prepare/index.scss   /my/outside/md/styles/index.css   """

    ## copy back
    #cpc = """cp  /my/outside/md/styles/index.css   ~/workspace/gg.intro/pyb/config/styles/index.css """
    #cpcssmap = """cp  /my/outside/md/styles/index.css.map   ~/workspace/gg.intro/pyb/config/styles/ """
    ## copy to gg2/srv/public
    #cpcgg2 = """cp  /my/outside/md/styles/index.css  ~/workspace/gg2/srv/public/stylesheets/index.css """
    #cpcssmapgg2 = """cp  /my/outside/md/styles/index.css.map ~/workspace/gg2/srv/public/stylesheets/ """

    #print(subprocess.call(cmdj.split(), shell=True))

    subprocess.call(cmdj, shell=True)
    subprocess.call(cpj, shell=True)
    subprocess.call(cpjgg2, shell=True)

    compile_css()

    #subprocess.call(cmdcss, shell=True)
    #subprocess.call(cpc, shell=True)
    #subprocess.call(cpcssmap, shell=True)
    #subprocess.call(cpcgg2, shell=True)
    #subprocess.call(cpcssmapgg2, shell=True)
    #pass



def compile_css():
    """I have to write commands in one line and use subprocess.call
    """

    cmdcss = """scss ~/workspace/gg.intro/pyb/config/prepare/index.scss   /my/outside/md/styles/index.css   """

    # copy back
    cpc = """cp  /my/outside/md/styles/index.css   ~/workspace/gg.intro/pyb/config/styles/index.css """
    cpcssmap = """cp  /my/outside/md/styles/index.css.map   ~/workspace/gg.intro/pyb/config/styles/ """
    # copy to gg2/srv/public
    cpc2gg2 = """cp  /my/outside/md/styles/index.css  ~/workspace/gg2/srv/public/stylesheets/index.css """
    cpcssmap2gg2 = """cp  /my/outside/md/styles/index.css.map ~/workspace/gg2/srv/public/stylesheets/ """

    #print(subprocess.call(cmdj.split(), shell=True))

    #return [cmdcss, cpc, cpcssmap, cpc2gg2, cpcssmap2gg2]

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
    pass



if __name__ == "__main__":

    compile_js_css()
    #compile_css()
