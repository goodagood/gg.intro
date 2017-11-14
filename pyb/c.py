
# check things

import a


if __name__ == "__main__":
    #a.mkmd(src='/tmp/b.md', dst='/tmp/b.cn.html')

    s = a.mkmd(src='/tmp/b.md')
    print(s[300:800])
