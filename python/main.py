import sys
import os
import shutil
import glob
sys.path.append('./src')
from application import Application

dirname  = input('Provide the directory name you put the JSON file in: ').strip()
filename = input('Provide the filename of which JSON data name you would like to sort: ').strip()
order    = input('Provide asc(default) or desc you would like to sort key-value in: ').strip()

params = dict()
for key, value in { 'dirname': dirname, 'filename': filename, 'order': order }.items():
    if value:
        params[key] = value

Application(**params).run()

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
