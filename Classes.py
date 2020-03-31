class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return("{} {}".format(emp_1.first, emp_1.last))
        
emp_1 = Employee("John", "Smith", 100000)
emp_2 = Employee("Jack", "Blog", 90000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())

print(Employee.fullname(emp_1))


    
