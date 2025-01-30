# TODO: Подробно описать три произвольных класса
import doctest


# TODO: описать класс
class ResidentialHouse:
    """
    Класс, описывающий жилой дом.

    Attributes:
        address (str): Адрес дома.
        num_floors (int): Количество этажей. Должно быть положительным числом.
        has_garden (bool): Наличие сада.
    """

    def __init__(self, address: str, num_floors: int, has_garden: bool = False):
        """
        Инициализация объекта класса ResidentialHouse.

        Args:
            address (str): Адрес дома.
            num_floors (int): Количество этажей.
            has_garden (bool, optional): Наличие сада. Defaults to False.

        Raises:
            ValueError: Если количество этажей не положительное число.
        """
        if num_floors <= 0:
            raise ValueError("Количество этажей должно быть положительным числом.")
        self.address: str = address
        self.num_floors: int = num_floors
        self.has_garden: bool = has_garden

    def get_info(self) -> str:
        """
        Возвращает информацию о доме в виде строки.

        Returns:
            str: Информация о доме.

        >>> house = ResidentialHouse("Улица Ленина, 10", 3)
        >>> house.get_info()
        'Адрес: Улица Ленина, 10, Этажей: 3, Сад: Нет'
        """
        garden_info = "Да" if self.has_garden else "Нет"
        return f"Адрес: {self.address}, Этажей: {self.num_floors}, Сад: {garden_info}"

    def change_garden_status(self, has_garden: bool) -> None:
        """
        Меняет статус наличия сада.

        Args:
            has_garden (bool): Новый статус.

        Returns:
            None
        """
        self.has_garden = has_garden

# TODO: описать ещё класс
class Car:
    """
    Класс, описывающий автомобиль.

    Attributes:
        make (str): Производитель автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля. Должен быть не больше текущего года.
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация объекта класса Car.

        Args:
            make (str): Производитель.
            model (str): Модель.
            year (int): Год выпуска.

        Raises:
            ValueError: Если год выпуска больше текущего.
        """
        from datetime import datetime
        if year > datetime.now().year:
            raise ValueError("Год выпуска не может быть больше текущего года.")
        self.make: str = make
        self.model: str = model
        self.year: int = year

    def get_info(self) -> str:
        """
        Возвращает информацию об автомобиле.

        Returns:
            str: Информация об автомобиле.

        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.get_info()
        'Toyota Camry, 2020'
        """
        return f"{self.make} {self.model}, {self.year}"

    def update_year(self, new_year: int) -> None:
        """
        Обновляет год выпуска автомобиля.

        Args:
            new_year (int): Новый год выпуска.

        Raises:
            ValueError: Если новый год больше текущего.
        """
        from datetime import datetime
        if new_year > datetime.now().year:
            raise ValueError("Год выпуска не может быть больше текущего года.")
        self.year = new_year

# TODO: и ещё один
class GameAccount:
    """
    Класс, описывающий игровой аккаунт.

    Attributes:
        username (str): Имя пользователя.
        level (int): Уровень игрока. Должен быть неотрицательным.
        score (int): Очки игрока. Должны быть неотрицательными.
    """

    def __init__(self, username: str, level: int = 0, score: int = 0):
        """
        Инициализация объекта класса GameAccount.

        Args:
            username (str): Имя пользователя.
            level (int, optional): Уровень игрока. Defaults to 0.
            score (int, optional): Очки игрока. Defaults to 0.

        Raises:
            ValueError: Если уровень или очки отрицательные.
        """
        if level < 0 or score < 0:
            raise ValueError("Уровень и очки должны быть неотрицательными.")
        self.username: str = username
        self.level: int = level
        self.score: int = score

    def level_up(self) -> None:
        """
        Повышает уровень игрока на 1.

        Returns:
            None
        """
        self.level += 1

    def add_score(self, points: int) -> int:
        """
        Добавляет очки игроку.

        Args:
            points (int): Количество добавляемых очков. Должно быть положительным.

        Returns:
            int: Новый общий счет.

        Raises:
            ValueError: Если количество очков отрицательное.

        >>> account = GameAccount("Player1", 1, 50)
        >>> account.add_score(10)
        60
        """
        if points < 0:
            raise ValueError("Количество очков должно быть положительным.")
        self.score += points
        return self.score

if __name__ == "__main__":
    doctest.testmod()
    
