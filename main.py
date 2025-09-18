# main.py

from animals import Bird, Mammal, Reptile
from employees import ZooKeeper, Veterinarian
from zoo import Zoo

# 3. Демонстрация полиморфизма
def animal_sound(animals_list):
    """
    Эта функция принимает список животных и вызывает метод make_sound() для каждого.
    Она не знает, какой именно тип животного в списке, но код работает благодаря полиморфизму.
    """
    print("\n--- Демонстрация полиморфизма ---")
    for animal in animals_list:
        animal.make_sound()

# --- Основная часть программы ---
if __name__ == "__main__":
    # Создаем экземпляры животных
    leo = Mammal("Лев Лео", 5, "золотистый")
    polly = Bird("Попугай Полли", 2, 0.4)
    karl = Reptile("Крокодил Карл", 10, is_venomous=False)

    # Демонстрируем полиморфизм
    all_animals = [leo, polly, karl]
    animal_sound(all_animals) # Вызываем функцию

    # Создаем зоопарк и сотрудников
    my_zoo = Zoo("Центральный Зоопарк")
    keeper_ivan = ZooKeeper("Иван")
    vet_maria = Veterinarian("Мария")

    # Добавляем животных и сотрудников в зоопарк (демонстрация композиции)
    my_zoo.add_animal(leo)
    my_zoo.add_animal(polly)
    my_zoo.add_animal(karl)
    my_zoo.add_employee(keeper_ivan)
    my_zoo.add_employee(vet_maria)

    # Показываем информацию
    my_zoo.show_all_animals()
    my_zoo.show_all_employees()

    # Демонстрируем взаимодействие объектов
    print("\n--- Взаимодействие объектов ---")
    keeper_ivan.feed_animal(leo)
    vet_maria.heal_animal(polly)
    
    # Демонстрация сохранения и загрузки
    print("\n--- Сохранение и загрузка ---")
    my_zoo.save_to_file("zoo_data.json")
    
    # Загружаем зоопарк в новый объект, чтобы показать, что данные восстановились
    loaded_zoo = Zoo.load_from_file("zoo_data.json")
    loaded_zoo.show_all_animals()
    loaded_zoo.show_all_employees()