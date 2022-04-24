class Employee:
    # self refers to the current instance of the class, used to access variable
    # that belongs to the class
    def setSalary(self, value):
        self.salary = value

e= Employee()
e.setSalary(2000)
print(e.salary)