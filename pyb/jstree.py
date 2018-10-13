
# build json data for jstree,
# https://github.com/vakata/jstree

import config_files
import mkindex


## !/usr/bin/python

import os
def showwalk(where="/my", saved=[], jstree=[]):
    for root, dirs, files in os.walk(where):
        print("---  ", root, dirs, files)
        jstree.append({"text":root, "id":root, "root":root,"type":"dir",
            "parent": "#"} )
        children = jstree[0]["children"]
        #jstree[0]["children"].append({"text":where, "type":"dir"} )

        for name in files:
            #print("files ")
            #print('file: ', os.path.join(root, name))
            full_path = os.path.join(root, name)
            saved.append(os.path.join(root, name))
            children.append({"text":name, "parent":root, "id":full_path} )
        for name in dirs:
            full_path = os.path.join(root, name)
            #print('dir: ', os.path.join(root, name))
            saved.append(os.path.join(root, name))
            children.append({"text":name, "type":"dir"} )
            children.append({"text":name, "parent":root, "id":full_path} )

            pass
        pass
    return saved


def empty_array(a):
    if type(a) != list:
        return False
    if len(a) = 0:
        return True

    return False


def contain(pa, pb):
    """if path pb is direct sub-element of path pa
    """
    pass



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

