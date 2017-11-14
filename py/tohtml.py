
import markdown

#html = markdown.markdown(your_text_string)


Path = '/home/za/workspace/gg.intro/md.files/intro.md'
CNPath = '/home/za/workspace/gg.intro/md.files/cn/intro.md'

def mkmd(src=Path, dst='/tmp/tmp.html'):
    with open(src, 'r') as f:
        fstr = f.read()


    html = markdown.markdown(fstr)
    with open(dst, 'w') as f:
        f.write(html)

    return html



if __name__ == "__main__":
    src = "/home/za/workspace/gg.intro/md.files"
    dst = "/home/za/workspace/gg.intro/py.pelican/content"

    mkmd()
    mkmd(src=CNPath, dst='/tmp/tmp.cn.html')
    mkmd(src='/tmp/b.md', dst='/tmp/b.cn.html')
