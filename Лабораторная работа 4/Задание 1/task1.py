# TODO: описать базовый класс
class MusicalWork:
    """
    Базовый класс для музыкальных произведений.

    Атрибуты:
        title (str): Название произведения.
        artist (str): Исполнитель произведения.
        year (int): Год выпуска произведения.
    """

    def __init__(self, title: str, artist: str, year: int) -> None:
        """
        Конструктор класса MusicalWork.

        :param title: Название произведения.
        :param artist: Исполнитель произведения.
        :param year: Год выпуска произведения.
        """
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление музыкального произведения."""
        return f"{self.title} by {self.artist} ({self.year})"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление музыкального произведения."""
        return f"MusicalWork(title='{self.title}', artist='{self.artist}', year={self.year})"

    def play(self) -> str:
        """
        Воспроизводит музыкальное произведение.

        :return: Строка, указывающая на воспроизведение произведения.
        """
        return f"Playing {self.title} by {self.artist}"

    def add_to_favorites(self) -> str:
        return f'{self.title!r} by {self.artist!r} has been added to favourites'
    """
    Унаследованный метод для дочернего класса Jazz
    """

# TODO: описать дочерний класс
class Jazz(MusicalWork):
    """
    Класс для джазовых музыкальных произведений, наследует от MusicalWork.

    Атрибуты:
        improvisation_level (int): Уровень импровизации в произведении (от 1 до 10).
    """

    def __init__(self, title: str, artist: str, year: int, improvisation_level: int) -> None:
        """
        Конструктор класса Jazz.

        :param title: Название джазового произведения.
        :param artist: Исполнитель джазового произведения.
        :param year: Год выпуска джазового произведения.
        :param improvisation_level: Уровень импровизации.
        """
        super().__init__(title, artist, year)
        self.__improvisation_level = improvisation_level  # Инкапсуляция для защиты атрибута

    def __str__(self) -> str:
        """Возвращает строковое представление джазового произведения с уровнем импровизации."""
        return f"{super().__str__()} with improvisation level of {self.__improvisation_level}"

    def play(self) -> str:
        """
        Воспроизводит джазовое произведение с добавлением информации об импровизации.

        :return: Строка, указывающая на воспроизведение джазового произведения.
        """
        return f"Playing {self.title} by {self.artist} - a jazz piece with improvisation level {self.__improvisation_level}"


print(Jazz('Caravan', 'Buddy Rich', 1962, 10).add_to_favorites()) #Пример работы унаследованного метода
