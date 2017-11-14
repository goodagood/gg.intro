
import tool


def cFind_md(dst):
    for p in tool.find_md(dst):
        print (p)



if __name__ == "__main__":
    src = "/home/za/workspace/gg.intro/md.files"
    dst = "/home/za/workspace/gg.intro/py.pelican/content"

    cFind_md(dst)
