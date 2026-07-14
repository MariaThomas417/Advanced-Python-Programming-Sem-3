class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee(201, "John", 45000)
e1.display()

"""
Employee ID: 201
Name: John
Salary: 45000
"""