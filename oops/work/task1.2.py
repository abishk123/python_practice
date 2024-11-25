# HYBRID INHERITANCE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id,sal):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = sal

    def show_employee_details(self):
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")
    
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def show_manager_details(self):
        print(f"Manager of {self.department} department")
    
class TechnicalEmployee(Employee):
    def __init__(self, name, age, employee_id, technical_skills):
        super().__init__(name, age, employee_id)
        self.technical_skills = technical_skills

    def show_technical_details(self):
        print(f"Technical Skills: {', '.join(self.technical_skills)}")

class TeamLead(Manager, TechnicalEmployee):
    def __init__(self, name, age, employee_id, department, technical_skills, team_size):
        Manager.__init__(self, name, age, employee_id, department)  # Explicit call to Manager's constructor
        TechnicalEmployee.__init__(self, name, age, employee_id, technical_skills)  # Explicit call to TechnicalEmployee's constructor
        self.team_size = team_size

    def show_teamlead_details(self):
        print(f"Team Lead of {self.team_size}-member team")

print(TeamLead.mro())
print()
print(TechnicalEmployee.mro())
print()
print(Manager.mro())