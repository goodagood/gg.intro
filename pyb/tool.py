
# Copy some util function from ../py/build.py
#


import os

import shutil
import copy
import errno

import sys
sys.path.append('../py')
import mdfile
import cmdargs



def copyfolder(src, dest):
    """src is an folder to be copied to dest as sub-folder

    dest will be removed before-hand if exists
    """
    name = os.path.basename(src)
    target = os.path.join(dest, name)

    if os.path.isdir(target):
        shutil.rmtree(target)

    shutil.copytree(src, target)



def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise



def find_md(dir='.'):
    for root,dirs,files in os.walk(dir):
        #print('-'*30)

        #print("\n")
        #print(root, dirs, files)
        #print("\n")

        for f in files:
            if mdfile.is_md_file(f):
                ppath = os.path.join(root, f)
                yield(ppath)

                #meta = meta_data(ppath,dir)
                ##print(ppath, meta)

                #yield(ppath, meta)

                ##print(os.path.basename(f))
                ##print(os.path.join(root, f))


# modify from same function in ../py/build.py
def check_parameter():
    args = cmdargs.get_args()
    clone = copy.copy(args)

    #print('>>>', args.source_dir, args.target_dir)

    if not clone.source_dir:
        clone.source_dir = './src'
        pass
    clone.source_dir = relative_to_abs_path(clone.source_dir)

    if not clone.target_dir:
        clone.target_dir = './build'

    clone.target_dir = relative_to_abs_path(clone.target_dir)

    # configuration path, currently py script path
    if not clone.conf:
        clone.conf = get_script_path()
    clone.conf = relative_to_abs_path(clone.conf)


    #clone.source_dir = os.path.abspath(clone.source_dir)
    #clone.target_dir = os.path.abspath(clone.target_dir)
    print('clone', clone)
    return clone


def get_script_path():
    script_path = None
    if __file__:
        script_path = os.path.dirname(os.path.abspath(__file__))
        print("script path : %s"%script_path)

    if not script_path:
        script_path = os.path.abspath(os.getcwd())
        print("cwd as script path : %s"%script_path)
        pass

    return script_path



def relative_to_abs_path(rpath):
    if rpath.startswith('/'):
        return rpath

    cwd = os.path.abspath(os.getcwd())

    full_path = os.path.join(cwd, rpath)
    abs_path  = os.path.abspath(full_path)

    #print("abs path after relative path to abs : %s"%abs_path)
    return abs_path



def mk_target_folder(mdsrc='.', tgt='/tmp/tgt'):


    # doing
    # source/target dir get from command line parameter -s -t
    param = check_parameter()
    if not param.source_dir:
        print('not source dir')
        return
    print('>source dir', param.source_dir)
    print('>target dir', param.target_dir)

    if param.delete_dir:
        shutil.rmtree(param.target_dir)
        print('rm target dir', param.target_dir)


    #?
    script_path = None
    if __file__:
        script_path = os.path.dirname(os.path.abspath(__file__))
        print("script path : %s"%script_path)

    if mdsrc == '.':
        pass





    cwd = os.getcwd()
    confPath = os.path.join(cwd, 'config')
    nmPath = os.path.join(cwd, 'config/node_modules')

    # copy node modules, there are css and js
    copyfolder(nmPath, tgt)

    # copy the bundle js file from config folder
    bundleJs = os.path.join(cwd, 'config/bundle.js')
    tBundleJs = os.path.join(tgt, 'bundle.js')
    print(bundleJs, tBundleJs)
    shutil.copy(bundleJs, tBundleJs)

    # styles
    stylePath = os.path.join(cwd, 'config/styles')
    copyfolder(stylePath, tgt)
    pass


def copy_js_css(cwd=None, tgt=None):
    if cwd == None:
        cwd = os.getcwd()
    if tgt == None:
        tgt = '/tmp/'

    # copy the bundle js file from config folder
    bundleJs = os.path.join(cwd, 'config/bundle.js')
    tBundleJs = os.path.join(tgt, 'bundle.js')
    print(bundleJs, tBundleJs)
    shutil.copy(bundleJs, tBundleJs)

    # styles
    stylePath = os.path.join(cwd, 'config/styles')
    copyfolder(stylePath, tgt)
    pass



if __name__ == "__main__":
    ooo = '/tmp/ooo'
    tgt = '/tmp/tgt'

    #mk_target_folder()
    #copyfolder(ooo, tgt)

    copy_js_css('/home/za/workspace/gg.intro/pyb/', '/my/outside/md')

