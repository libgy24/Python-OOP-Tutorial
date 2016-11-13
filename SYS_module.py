# import sys
#
# sys.version
#
# sys.copyright
#
# sys.executable
#
# sys.builtin_module_names
#
# sys.modules
#
# sys.modules.keys()
#
# sys.platform
#
# sys.stderr.write('testdaf\n')
# sys.stderr.flush()
#
# sys.stdout.write('This is a test output\n')
# sys.stdout.flush()


import time
import sys

for i in range(5):
    print (i)
    sys.stdout.flush()
    time.sleep(1)

print(sys.argv)