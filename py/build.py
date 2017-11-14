
# build static website directly


import os
import shutil
import copy
from datetime import datetime

import distutils.dir_util as dutil


import mdfile
import cmdargs


def find_md(dir='.'):
    for root,dirs,files in os.walk(dir):
        #print('-'*30)

        #print("\n")
        #print(root, dirs, files)
        #print("\n")

        for f in files:
            if mdfile.is_md_file(f):
                ppath = os.path.join(root, f)
                meta = meta_data(ppath,dir)
                #print(ppath, meta)

                yield(ppath, meta)

                #print(os.path.basename(f))
                #print(os.path.join(root, f))


Meta_template = """    Title: {title}
    Date: {date}
    Author: Andrew
    

"""

Meta_template_dash = """---
Title: {title}
Date: {date}
Author: Andrew
---


"""

def meta_data(ppath, dir):
    file_name = os.path.basename(ppath)

    relpath = os.path.relpath(ppath, dir)

    if relpath:
        print ('relpath: ', relpath)
        path_no_file_name = os.path.dirname(relpath)

        if path_no_file_name:
            print( 'path_no_file_name:', path_no_file_name)
            tag = path_no_file_name.replace('/', '__')

            file_name += ("__" + tag)

    try:
        mtime = os.path.getmtime(ppath)
    except OSError:
        mtime = 0

    last_modified_date = datetime.fromtimestamp(mtime)

    meta = Meta_template.format(title=file_name, date=last_modified_date)

    return meta


def ccopy(src, dest):
    dutil.copy_tree(src, dest)


def check_parameter():
    args = cmdargs.get_args()
    clone = copy.copy(args)

    print('>>>', args.source_dir, args.target_dir)

    src = args.source_dir
    tgt = args.target_dir

    if not clone.source_dir:
        clone.source_dir = './src'

    if not clone.target_dir:
        clone.target_dir = './build'

    clone.source_dir = os.path.abspath(clone.source_dir)
    clone.target_dir = os.path.abspath(clone.target_dir)
    return clone


def add_meta(ppath, meta):
    with open(ppath, 'r+') as f:
        fstr = f.read()
        fstr = meta + fstr

        f.seek(0)
        f.write(fstr)
        f.truncate()
        f.close()
        pass


def process():

    # source/target dir
    param = check_parameter()
    if param.delete:
        shutil.rmtree(param.target_dir)

    ccopy(param.source_dir, param.target_dir)

    # find markdown files and do it
    for ppath,meta in find_md(param.target_dir):
        print(ppath, "\n", meta)
        #add_meta(ppath, meta)


def cFind_md(dst):
    for p,m in find_md(dst):
        print (p, m)

if __name__ == "__main__":
    src = "/home/za/workspace/gg.intro/md.files"
    dst = "/home/za/workspace/gg.intro/py.pelican/content"

    #ccopy(src, dst)

    #find_md(dst)

    #print('[src]', s, '[tgt]',t)

    #cFind_md(dst)

    #add_meta('/tmp/mxargs', "oo\noo\n")
    process()
