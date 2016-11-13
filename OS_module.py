import os

print(os.getcwd())

cwd = "/Users/Zhengyi/Documents/Python/Python for Data Science/Python OOP Tutorial"
print(cwd)

print(os.chdir('/Users/Zhengyi/Desktop/'))

print(os.chdir(cwd))

os.makedirs('os-demo_2/dub_dir-1') # os.makedirs will create folder and subfoder
os.mkdir('os-demo-2') # os.mkdir cannot create subfolder

os.removedirs('os-demo_2/dub_dir-1') # os.removedirs will delete all folders
os.rmdir('os-demo-2')

os.rename('test.txt', 'new_name.txt')

os.state('new_name.txt')

import datetime as dt

m_time = os.stat('new_name.txt').st_mtime

print(os.stat('new_name.txt').st_mtime)

dt.datetime.fromtimestamp(m_time)

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:',dirnames)
    print('Files:', filenames)
    print()

os.environ.get('HOME')

os.path.join(os.environ.get('HOME'), 'text.txt')

os.path.basename('temp/text.txt')

os.path.dirname('temp/text.txt')

os.path.split('temp/test.txt')

os.path.exists('temp/test.txt')

os.path.isdir('temp/test.txt')

os.path.splitext('temp/test.txt')

print(dir(os.path))