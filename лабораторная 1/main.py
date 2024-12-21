from task_1 import ResidentialHouse, Car, GameAccount # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
 house = ResidentialHouse("Улица Ленина, 10", 3)
 car = Car("Toyota", "Camry", 2020)
 account = GameAccount("Player1", 1, 50)

try:
    bad_house = ResidentialHouse("Улица Пушкина, 5", -1)
except ValueError as e:
    print(f"Ошибка: неправильные данные")

try:
    bad_car = Car("Ford", "Mustang", 2025)  # Год в будущем
except ValueError as e:
    print(f"Ошибка: неправильные данные")

try:
    bad_account = GameAccount("Player2", -1, 50)  # Отрицательный уровень
    account.add_score(-10)  # Отрицательные очки
except ValueError as e:
    print(f"Ошибка: неправильные данные")