class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Name: {self.name}, ID: {self.emp_id}"


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def get_info(self):
        return super().get_info() + f", Department: {self.department}"

    def manage_project(self, project_name):
        return f"Manager {self.name} is managing the project: {project_name}"


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def get_info(self):
        return super().get_info() + f", Specialization: {self.specialization}"

    def perform_maintenance(self, equipment):
        return f"Technician {self.name} is performing maintenance on: {equipment}"


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)
        return f"Employee {employee.name} added to {self.name}'s team."

    def get_team_info(self):
        if not self.team:
            return f"{self.name} has no team members."
        return "\n".join([member.get_info() for member in self.team])


# Демонстрация
# Создание объектов
employee = Employee("Alice", 101)
manager = Manager("Bob", 102, "HR")
technician = Technician("Charlie", 103, "Networking")
tech_manager = TechManager("Diana", 104, "IT", "Systems Administration")

# Демонстрация функциональности
print(employee.get_info())
print(manager.get_info())
print(manager.manage_project("Recruitment Drive"))
print(technician.get_info())
print(technician.perform_maintenance("Router"))

# TechManager функциональность
print(tech_manager.get_info())
print(tech_manager.manage_project("Infrastructure Upgrade"))
print(tech_manager.perform_maintenance("Server"))
print(tech_manager.add_employee(employee))
print(tech_manager.add_employee(technician))
print(tech_manager.get_team_info())