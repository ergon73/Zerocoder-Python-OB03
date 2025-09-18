# animals.py

# 1. Создание базового класса Animal
class Animal:
    """
    Базовый класс для всех животных в зоопарке.
    Содержит общие атрибуты и методы.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        """Общий метод для издания звука."""
        print(f"{self.name} издает какой-то звук.")

    def eat(self):
        """Общий метод для приема пищи."""
        print(f"{self.name} ест.")
        
    def __str__(self):
        """Строковое представление объекта для удобного вывода."""
        return f"{self.name}, возраст: {self.age}"

# 2. Реализация наследования: создание подклассов
class Bird(Animal):
    """
    Подкласс для птиц. Наследуется от Animal.
    """
    def __init__(self, name, age, wing_span):
        # super().__init__() вызывает конструктор родительского класса Animal
        super().__init__(name, age)
        self.wing_span = wing_span # Специфический атрибут для птиц

    # Переопределение метода родительского класса
    def make_sound(self):
        print(f"{self.name} чирикает 'Чирик-чирик!'")

class Mammal(Animal):
    """
    Подкласс для млекопитающих. Наследуется от Animal.
    """
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color # Специфический атрибут

    def make_sound(self):
        print(f"{self.name} рычит 'Ррррр!'")

class Reptile(Animal):
    """
    Подкласс для рептилий. Наследуется от Animal.
    """
    def __init__(self, name, age, is_venomous):
        super().__init__(name, age)
        self.is_venomous = is_venomous # Специфический атрибут

    def make_sound(self):
        print(f"{self.name} шипит 'Шшшшш!'")