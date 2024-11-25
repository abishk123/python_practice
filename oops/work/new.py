class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Name: {self.name}, Age: {self.age}"

# Class Employee (Inherits from Person - Single Inheritance)
class Employee(Person):
    def __init__(self, name, age, employee_id,sal):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = sal

    def show_employee_details(self):
        return f"Employee ID: {self.employee_id}, Salary: {self.salary}"

# Class Manager (Inherits from Employee - Multilevel Inheritance)
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def show_manager_details(self):
        return f"Manager of {self.department} department"

# Class TechnicalEmployee (Inherits from Employee - Multilevel Inheritance)
class TechnicalEmployee(Employee):
    def __init__(self, name, age, employee_id, technical_skills):
        super().__init__(name, age, employee_id)
        self.technical_skills = technical_skills

    def show_technical_details(self):
        return f"Technical Skills: {', '.join(self.technical_skills)}"

# Class TeamLead (Hybrid Inheritance)
# Inherits from both Manager and TechnicalEmployee
class TeamLead(Manager, TechnicalEmployee):
    def __init__(self, name, age, employee_id, department, technical_skills, team_size):
        Manager.__init__(self, name, age, employee_id, department)  # Explicit call to Manager's constructor
        TechnicalEmployee.__init__(self, name, age, employee_id, technical_skills)  # Explicit call to TechnicalEmployee's constructor
        self.team_size = team_size

    def show_teamlead_details(self):
        return f"Team Lead of {self.team_size}-member team"

# Create instances of different classes
person = Person("John Doe", 35)
employee = Employee("Alice", 28, "E12345")
manager = Manager("Bob", 40, "M98765", "Sales")
tech_employee = TechnicalEmployee("Charlie", 32, "T54321", ["Python", "Machine Learning", "Data Analysis"])
team_lead = TeamLead("David", 30, "TL11223", "Engineering", ["Python", "DevOps", "Cloud Computing"], 8)

# Output the details
print(person.show_details())  # Name: John Doe, Age: 35
print(employee.show_details(), employee.show_employee_details())  # Name: Alice, Age: 28; Employee ID: E12345, Salary: 50000
print(manager.show_details(), manager.show_employee_details(), manager.show_manager_details())  # Manager of Sales department
print(tech_employee.show_details(), tech_employee.show_employee_details(), tech_employee.show_technical_details())  # Technical Skills: Python, Machine Learning, Data Analysis
print(team_lead.show_details(), team_lead.show_employee_details(), team_lead.show_manager_details(), team_lead.show_technical_details(), team_lead.show_teamlead_details())
# Output: