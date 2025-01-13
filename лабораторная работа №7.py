class Employee:
    def __init__(self, name, id, **kwargs):
        self.name = name
        self.id = id

    def get_info(self):
        return f'Имя: {self.name}, ID: {self.id}'

class Manager(Employee):
    def __init__(self, name, id, department, **kwargs):
        super().__init__(name, id, **kwargs)
        self.department = department

    def get_info(self):
        return f'Имя: {self.name}, ID: {self.id}, Отдел: {self.department}'

    def manage_project(self):
        return f"{self.name} управляет проектом в {self.department}."


class Technician(Employee):
    def __init__(self, name, id, specialization, **kwargs):
        super().__init__(name, id, **kwargs)
        self.specialization = specialization

    def get_info(self):
        return f'Имя: {self.name}, ID: {self.id}, Специализация: {self.specialization}'

    def perform_maintenance(self):
        return f'{self.name} Специализация: {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        super().__init__(name=name, id=id, department=department, specialization=specialization)
        self.information = []

    def add_employee(self, employee):
        self.information.append(employee)

    def get_team_info(self):
        for s in self.information:
            print(s.get_info())


s1 = Manager('Olya', 11253, 'HGH')
s2 = Technician('Gosha',63394, 'GHJG')
TM = TechManager('hgh', 16468681, '46387', '6328')
TM.add_employee(s1)
TM.add_employee(s2)
print(s2.perform_maintenance())
print(s1.manage_project())
print(TM.get_info())
TM.get_team_info()






