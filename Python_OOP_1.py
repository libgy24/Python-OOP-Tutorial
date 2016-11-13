# Python Object-Oriented Programming

class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

print(type(emp_1))
print(emp_2)

emp_1.first = 'Zhengyi'
emp_1.last = 'Li'
emp_1.email = 'zli@company.com'
emp_1.pay = 10000000000000000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test.user@company.com'
emp_2.pay = 90000000000000000

print(emp_1.email)
print(emp_2.email)


class employee_1:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp_1 = employee_1('Zhengyi', 'Li', 1000000)
emp_2 = employee_1('Test', 'User', 2000000)


print(emp_1.pay)
print(emp_2.pay)
print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())


employee_1.fullname(emp_1)