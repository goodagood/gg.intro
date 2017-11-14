
import os

import tool


def mkfolder(fpath):
    #filename = os.path.basename(fpath)
    #no_ext = os.path.splitext(filename)[0]
    #print("file name: %s, no ext: %s, path: %s"%(filename, no_ext, fno_ext))

    folder_path = os.path.splitext(fpath)[0]
    print("folder  path: %s"%(folder_path))

    tool.mkdir_p(folder_path)


def md_index_html(md_abs_name):
    mkfolder(md_abs_name)
    folder_path = os.path.splitext(md_abs_name)[0]
    abs_index_html = os.path.join(folder_path, 'index.html')
    return abs_index_html





if __name__ == "__main__":
    mkfolder('/tmp/ooo/tgt/some/folder/file.ext')
    mkfolder('/tmp/ooo/tgt/some/folder/filename')
