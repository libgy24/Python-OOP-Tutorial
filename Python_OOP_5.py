# Special (Magic/Dunder) Methods


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.last, self.first)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')


    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None



emp_1 = Employee('Zhengyi', 'Li', 1000000000)
emp_2 = Employee('Test', 'Employee', 20000000000)

print(repr(emp_1))

print(str(emp_1))

print(emp_1 + emp_2)

print(len(emp_1))

emp_1.fullname = 'Test User2'