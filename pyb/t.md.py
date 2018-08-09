
import os

import mkmd
import tool

print(type(mkmd.render_html))


#mkmd.render_html('/tmp/some',  '/tmp/b.html')

#mkmd.md2html_same_folder ('/tmp/some')



template = './template/template.html'

src = "/tmp/story/y10m/b.markdown"
tgt = "/my/outside/tmp/tmp.html"

sp = tool.find_script_path()
print("sp script path: ", sp)

template_abs = os.path.join(sp, template)

mkmd.mkhtml(template=template_abs, src=src, dst=tgt)








