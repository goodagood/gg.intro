
import glob
import re
import os
import os.path as path

import cmdargs


def is_md_file(filename):
    exts = ['.+\.markdown$', '.+\.md$', '.+\.mkd$']
    res  = [re.compile(ext, re.I) for ext in exts]
    for r in res:
        m = r.match(filename)
        if m:
            #print(m)
            return m

    return False



def make_conf():
    args = cmdargs.get_args()

    conf = {
            "dir": "md.files",
            "dirA": "front.pages",
            "dirB": "design",
            "dirs": ["front.pages", "design"]
            }

    conf['cwd'] = os.getcwd()

    if type(args.cwd) == str:
        conf['cwd'] = args.cwd
    if type(args.source_dir) == str:
        conf['dir'] = args.source_dir

    conf['absDir'] = path.join(conf['cwd'], conf['dir'])

    return conf



def get_md_file(pat="*.md"):
    conf = make_conf()

    if conf['cwd'] != os.getcwd():
        os.chdir(conf['absDir'])

    mds = glob.iglob(pat)

    for m in mds:
        print(m)
    #print(mds)
    pass



if __name__ == "__main__":
    print(os.getcwd())
    #get_md_file()

    print(is_md_file('tmp.mD'))

