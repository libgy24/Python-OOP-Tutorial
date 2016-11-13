# Class variable and Instance variable

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, last, first, pay):
        self.last = last
        self.first = first
        self.pay = pay
        self.email = last + '.' + first + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.last, self.first)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Zhengyi', 'Li', 1000000)
emp_2 = Employee('Test', 'User', 2000000)

# Class variables are variables shared among all instances in a class
# and it should be same for all instances

emp_1.apply_raise()
print(emp_1.pay)
Employee.raise_amount = 1.04

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
emp_1.raise_amount = 1.06

print(emp_1.pay)
print(emp_1.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)