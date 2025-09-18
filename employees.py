# employees.py

class Employee:
    """Базовый класс для всех сотрудников."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Сотрудник: {self.name}"

class ZooKeeper(Employee):
    """Класс для смотрителя зоопарка."""
    def feed_animal(self, animal):
        # Этот метод принимает объект животного и выполняет с ним действие
        print(f"Смотритель {self.name} кормит {animal.name}.")

class Veterinarian(Employee):
    """Класс для ветеринара."""
    def heal_animal(self, animal):
        print(f"Ветеринар {self.name} лечит {animal.name}.")