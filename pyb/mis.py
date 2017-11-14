
import os

os.path.expanduser('~')
os.path.expanduser('~/some/dir')


import pystache
h = pystache.render('Hi {{person}}!', {'person': 'Mom'})
print(h)
