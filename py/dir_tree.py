
import os
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


Meta_template = """Title: {title}
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


def get_dir_param():
    args = cmdargs.get_args()
    print('>>>', args.source_dir, args.target_dir)

    src = args.source_dir
    tgt = args.target_dir

    if not src:
        src = '.'

    if not tgt:
        raise Exception('no target dir, do it --target-dir ...')

    src = os.path.abspath(src)
    tgt = os.path.abspath(tgt)
    return (src,tgt)


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
    src,tgt = get_dir_param()
    ccopy(src, tgt)

    # find markdown files and do it
    for ppath,meta in find_md(tgt):
        print(ppath, "\n", meta)
        add_meta(ppath, meta)


def cFind_md(dst):
    for p,m in find_md(dst):
        print (p, m)

if __name__ == "__main__":
    src = "/home/za/workspace/gg.intro/md.files"
    dst = "/home/za/workspace/gg.intro/py.pelican/content"

    #ccopy(src, dst)

    #find_md(dst)

    #(s,t) = get_dir_param()
    #print('[src]', s, '[tgt]',t)

    #cFind_md(dst)

    #add_meta('/tmp/mxargs', "oo\noo\n")
    process()
