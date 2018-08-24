
# check things

import config_files
import mkindex


if __name__ == "__main__":

    print(config_files.En_lang_switch)

    #mkindex.dotemplate( ... )

    # cn index
    mkindex.dotemplate(
            mdsrc   =config_files.Cn_index_md, 
            tplsrc  =config_files.Index_template,
            dst     =config_files.Cn_index_dst, 
            htmlRoot=config_files.HTMLRoot,
            lang_tag=config_files.En_lang_switch)  # en page get a cn switch, vice versa

    # en index
    mkindex.dotemplate(
            mdsrc   =config_files.En_index_md, 
            tplsrc  =config_files.Index_template,
            dst     =config_files.En_index_dst, 
            htmlRoot=config_files.HTMLRoot,
            lang_tag=config_files.Cn_lang_switch)  # en page get a cn switch, vice versa

    pass

