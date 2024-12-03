class Employee:
    def __init__(self, name, position, salary, experience_level, skills):
        self.name = name
        self.position = position
        self.salary = salary
        self.experience_level = experience_level
        self.skills = skills

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Должность: {self.position}")
        print(f"Зарплата: {self.salary}")
        print(f"Уровень опыта: {self.experience_level}")
        print(f"Дополнительные навыки: {', '.join(self.skills)}")

    def promote(self, new_position, salary_increase):
        self.position = new_position
        self.salary += salary_increase
        print(f"{self.name} переведён на новую должность - {new_position}.")
        print(f"Новая зарплата: {self.salary} рублей.")

employee1 = Employee("Иван Иванов", "Менеджер", 50000, "Средний", ["Управление проектами", "Командная работа"])
employee2 = Employee("Анна Янина", "Разработчик", 60000, "Высокий", ["Python", "Дизайн", "Командная работа"])

employee1.display_info()
employee1.promote("Старший менеджер", 10000)
print()
employee2.display_info()
employee2.promote("Ведущий разработчик", 25000)
