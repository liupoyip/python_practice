import path_manager
import os
import sys
from modules import hello, world
import foo


dir_data = 'data'
data_list = os.listdir(os.path.join('.', dir_data))

print('show sys.path: ', end='\n    ')
print('\n    '.join([_ for _ in sys.path]))
print()
print('show imported modules: ', end='\n    ')
print('\n    '.join([_ for _ in sys.modules.keys()]))
