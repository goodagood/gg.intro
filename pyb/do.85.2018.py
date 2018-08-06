
import os
import subprocess


import compile_js_css
import mkmd
import mkindex

TargetRoot = "/tmp/tr"

MDSrc = os.path.expanduser("~/workspace/gg.intro/md.files")




#
# It should be clear to set all target now.
#

print(MDSrc, TargetRoot )


compile_js_css.js_folders(1,2)




