import os
os.chdir('/Users/Zhengyi/Desktop')

old_path = '/Users/Zhengyi/Documents/Python/Python for Data Science/Python OOP Tutorial'

os.listdir(os.getcwd())


for f in os.listdir():
    filename, extension = os.path.splitext(f)
    print(filename.split('_'))