
# check things

import config_files
import mkindex


## !/usr/bin/python

import os
def showwalk(where="/my", saved=[]):
    for root, dirs, files in os.walk(where):
        print("---  ", root, dirs, files)
        for name in files:
            #print("files ")
            #print('file: ', os.path.join(root, name))
            saved.append(os.path.join(root, name))
        for name in dirs:
            #print('dir: ', os.path.join(root, name))
            saved.append(os.path.join(root, name))

            pass
        pass
    return saved


if __name__ == "__main__":
    where = "/my/outside/sept"

    print(config_files.En_lang_switch)


    tree = []
    s = showwalk(where=where, saved=tree)

    #mkindex.dotemplate( ... )

    ## cn index
    #mkindex.dotemplate(
    #        mdsrc   =config_files.Cn_index_md, 
    #        tplsrc  =config_files.Index_template,
    #        dst     =config_files.Cn_index_dst, 
    #        htmlRoot=config_files.HTMLRoot,
    #        lang_tag=config_files.En_lang_switch)  # en page get a cn switch, vice versa

    ## en index
    #mkindex.dotemplate(
    #        mdsrc   =config_files.En_index_md, 
    #        tplsrc  =config_files.Index_template,
    #        dst     =config_files.En_index_dst, 
    #        htmlRoot=config_files.HTMLRoot,
    #        lang_tag=config_files.Cn_lang_switch)  # en page get a cn switch, vice versa

    pass

