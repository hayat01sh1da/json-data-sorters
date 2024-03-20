import sys
sys.path.append('./src')
import os
from application import Application

dirname  = os.path.join('..', 'json')
if len(sys.argv) == 2:
    _, filename = sys.argv
else:
    filename = ''
filepath = os.path.join(dirname, filename)

print('Start exporting JSON data in {filepath}'.format(filepath = filepath))
Application(dirname, filename).run()
print('Done exporting JSON data in {filepath} 🎉'.format(filepath = filepath))
