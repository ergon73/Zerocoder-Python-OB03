# zoo.py

import json # Модуль для работы с файлами формата JSON

# Импортируем наши классы, чтобы можно было с ними работать
from animals import Bird, Mammal, Reptile
from employees import ZooKeeper, Veterinarian

class Zoo:
    """
    Класс Zoo использует композицию: он содержит списки объектов животных и сотрудников.
    """
    def __init__(self, name):
        self.name = name
        self.animals = []      # Список для хранения объектов животных
        self.employees = []    # Список для хранения объектов сотрудников

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"В зоопарк '{self.name}' добавлено новое животное: {animal.name}.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"В зоопарк '{self.name}' нанят новый сотрудник: {employee.name}.")

    def show_all_animals(self):
        print(f"\n--- Животные в зоопарке '{self.name}' ---")
        for animal in self.animals:
            print(f"- {animal}")
            
    def show_all_employees(self):
        print(f"\n--- Сотрудники в зоопарке '{self.name}' ---")
        for employee in self.employees:
            print(f"- {employee}")

    # --- Дополнительное задание: Сохранение и загрузка ---
    
    def save_to_file(self, filename):
        """Сохраняет состояние зоопарка в файл."""
        zoo_data = {
            "name": self.name,
            "animals": [],
            "employees": []
        }
        
        for animal in self.animals:
            # Преобразуем объект в словарь, чтобы его можно было сохранить в JSON
            animal_info = {"type": type(animal).__name__, "name": animal.name, "age": animal.age}
            if isinstance(animal, Bird):
                animal_info["wing_span"] = animal.wing_span
            elif isinstance(animal, Mammal):
                animal_info["fur_color"] = animal.fur_color
            elif isinstance(animal, Reptile):
                animal_info["is_venomous"] = animal.is_venomous
            zoo_data["animals"].append(animal_info)

        for emp in self.employees:
            emp_info = {"type": type(emp).__name__, "name": emp.name}
            zoo_data["employees"].append(emp_info)

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(zoo_data, f, indent=4, ensure_ascii=False)
        print(f"Зоопарк '{self.name}' сохранен в файл {filename}.")

    @classmethod
    def load_from_file(cls, filename):
        """Загружает состояние зоопарка из файла и создает новый объект Zoo."""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        zoo = cls(data["name"])

        for animal_info in data["animals"]:
            animal_type = animal_info.pop("type")
            if animal_type == "Bird":
                zoo.add_animal(Bird(**animal_info))
            elif animal_type == "Mammal":
                zoo.add_animal(Mammal(**animal_info))
            elif animal_type == "Reptile":
                zoo.add_animal(Reptile(**animal_info))

        for emp_info in data["employees"]:
            emp_type = emp_info.pop("type")
            if emp_type == "ZooKeeper":
                zoo.add_employee(ZooKeeper(**emp_info))
            elif emp_type == "Veterinarian":
                zoo.add_employee(Veterinarian(**emp_info))

        print(f"Зоопарк '{zoo.name}' загружен из файла {filename}.")
        return zoo