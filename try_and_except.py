

try:
    f = open('test_output.txt')
  #  var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    file_c = f.readlines()
    print(file_c)
    f.close()
# else will execute if there is no exception;


try:
    f = open('test_output1.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    file_c = f.readlines()
    print(file_c)
    f.close()
finally:
    print('Executing finally...')
# finally will run whether or not there is an exception.


try:
    f = open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    file_c = f.readlines()
    print(file_c)
    f.close()
finally:
    print('Executing finally...')
# we can raise our own exception