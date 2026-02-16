#multilevel inheritance
#parent class
class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age
       
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
           
class Manager(Employee, Person):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        
    def display_manager_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Department:", self.department)
        
Manager = Manager("Sarman", 18, "ADT25SOCB1120" , 240000 ,"CSE" )
Manager.display_manager_info()
             
           
    