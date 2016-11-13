# Duck Typing and Easier to ask forgiveness than permission (EAFP).

class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap!')



class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    #Not Duck-Typed(Non-pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be a Duck!')

    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)



def add(x, y):
    pass

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    pass