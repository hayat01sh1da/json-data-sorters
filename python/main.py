import sys
import os
import shutil
import glob
sys.path.append('./src')
from application import Application

dirname  = input('Provide the directory name you put the JSON file in: ')
filename = input('Provide the filename of which JSON data name you would like to sort: ')
order    = input('Provide asc(default) or desc you would like to sort key-value in: ')

filepath = os.path.join(dirname, filename)

print('Start exporting JSON data in {filepath}'.format(filepath = filepath))
Application(dirname, filename, order).run()
print('Done exporting JSON data in {filepath} 🎉'.format(filepath = filepath))

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
