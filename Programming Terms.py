# First-Class Function:
# "A programming language is said to have first-class if it treats functions as first-class citizens."

# First-Class Citizen (Programming):
# A first-class citizen (sometimes called first-class objects) in a programming language is an entity which supports all the operations generally available to other entities.
# These operations typically include being passed as an argument, returned from a function, and assigned to a variable."

def square(x):
    return x * x

f = square

print(square)
print(f)

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)

def cube(x):
    return x * x * x

cubes = my_map(cube, [1, 2, 3, 4, 5])

print(cubes)

def logger(msg):
    def log_message():
        print('log:', msg)
    return log_message

log_hi = logger('Hi!')

log_hi()


def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')


employees = ['Corey', 'John', 'Rick', 'Steve', 'Carl', 'Adam']
output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}<li>'.format(employee)
    print('Address of Output is {}'.format(id(output)))

output +='</ul>'

print(output)

print('\n')


import time

ef_cache = {}


def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]

    print('Computing {}...'.format(num))
    time.sleep(1)
    result = num*num
    ef_cache[num] = result
    return result

print(expensive_func(4))

print(expensive_func(10))

print(expensive_func(4))

print(expensive_func(10))

print(expensive_func(4))

print(expensive_func(4))


# Closures

# A closure is a record storing a function together with
# an environment: a mapping associating each free variable of the function
# with the value or storage location to which the name was bound when
# the closure was created. A closure, unlike a plain function, allows
# the function to access those captured variables through the closure's
# reference to them , even when the function is invoked outside their scope.

def outer_func():
    message = "Hi"
    def inner_func():
        print(message)
    return inner_func



my_func = outer_func()


my_func()
my_func()
my_func()

def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('HI')
hello_func = outer_func('Hello')
hi_func()
hello_func()

import logging

logging.basicConfig(filename = 'example.log', level = logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args)
        )
        print(func(*args))
    return log_func

def  add(x, y):
    return x + y

def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)
add_logger(3, 3)


