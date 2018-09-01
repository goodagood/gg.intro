
import os

tmppath = "/home/andrew/workspace/gg.intro/template"
tp2     = "/home/andrew/test/one/public"
tp3     = "/tmp/oo"

def walk(folder="/home/andrew/workspace/gg.intro/template/js"):

    d0 = depth(folder)
    print()

    for path, dirs, files in os.walk(folder):
        d = depth(path)
        prefix = "|-- "*(d - d0 + 1)

        print(prefix + "DIR: " + path)

        prefix = prefix + "    "

        #for d in dirs:
        #    print( prefix + d)

        for f in files:
            print( prefix + f)


def depth(dir_path):
    return len(dir_path.split('/'))


print('call walk()')
walk(tp3)

