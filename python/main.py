import sys
sys.path.append('./src')
import os
from application import Application

filepath = os.path.join('.', 'json', 'users.json')

Application(filepath = filepath).run()
print('JSON data has been successfully exported in {filepath} 🎉'.format(filepath = filepath))
