# File object

#### read file

f = open('test.txt', 'r')

print(f.name)
print(f.mode)

# when we open a file , we have to explicitly close it.
# if we do not close the file, we may run out file descriptor in the system.
f.close()

# 'r': read flie
# 'w': write file
# 'a': append file
# 'r+': read and write file


# context manager allows us to work with files from within this block and
# after we exit the block, it automatically the file for us.
with open('test.txt', 'r') as f:
  #  f_contents = f.read()
    f_contents_1 = f.readlines()
 #   print(f_contents)
    print(f_contents_1)
# after we exist the block, we still have have access to the variable "f",
# but the file is closed. we cannot read it.


# it is efficient, because it does not all the content all in once.
with open('test.txt', 'r') as f:
    for line in f.readlines():
        print(line, end = '\t')


with open('test.txt', 'r') as f:
    f_contents = f.read(5) # this will grab the first 10 characters in the file
    print(f_contents)
    while len(f_contents) > 0:
        print(f_contents, end = '*')
        print(f.tell())
        f_contents = f.read(5)

with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end = "*")

    f.seek(0)
    while len(f_contents) > 0:
        f_contents = f.read(size_to_read)
        print(f_contents)
        f.seek(0) # return the pointer to the beginning, and this would never end.
        f_contents = f.read(size_to_read)


#### write file

with open('test2.txt', 'w') as f:
    f.write('This is a test file for python\n this is to test write mode')

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

with open('test.txt','r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf.readlines():
            wf.write(line)


# when we work with jpg file, we have to open the file in binary file
# we are going to read byte.
with open('mini.jpg', 'rb') as rf:
    with open('mini_copy.jpg', 'wb') as wf:
        for line in rf.readlines():
            wf.write(line)



