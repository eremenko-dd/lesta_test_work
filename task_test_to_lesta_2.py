from collections import deque


class ВequeBuferFIFO:
    """
    Класс ВequeBuferFIFO реализует циклический буфер FIFO (First-In-First-Out)
    c использованием модуля collections.
    Плюсы реализации:
    1. collections.deque быстрее для операций добавления и удаления элементов
    из начала списка, чем обычный список.
    2. Операции добавления и удаления элементов занимают O(1) времени, что
    делает эту реализацию эффективной для больших объемов данных.
    3. У collections.deque есть фиксированная длина буфера, что полезно для
    автоматического удаления старых элементов при превышении размера буфера.

    Минусы реализации:
    1. Использование collections.deque требует импорта модуля collections, что
    может быть неудобно, если вы стремитесь к минимальным зависимостям.
    """

    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def add_value(self, value):
        """Функция добавления значения в буфер"""

        self.buffer.append(value)

    def pop_value(self):
        """Функция извлечения крайнего с начала значения"""

        if not self.buffer:
            return "Буффер пуст"
        return self.buffer.popleft()

    def show_value(self):
        """Фунция показа содержимого буфера"""

        return list(self.buffer)

    def is_empty(self):
        """Функция очистки буфера"""

        self.buffer = []


class ListBuferFIFO:
    """
    Класс ListBuferFIFO реализует циклический буфер FIFO (First-In-First-Out)
    с помощью списков.
    Плюсы реализации:
    1. Простая реализация с использованием обычного списка.
    2. Не требует импорта дополнительных модулей.

    Минусы реализации:
    1. Операции добавления и удаления элементов из начала списка медленнее,
    чем у collections.deque, особенно при больших объемах данных (O(n) против
    O(1)).
    """

    def __init__(self, size):
        self.size = size
        self.buffer = []

    def add_value(self, item):
        """Функция добавления значения в буфер"""

        if len(self.buffer) == self.size:
            self.buffer.pop(0)
        self.buffer.append(item)

    def pop_value(self):
        """Функция извлечения крайнего с начала значения"""

        if not self.buffer:
            return "Буффер пуст"
        pop_value = self.buffer.pop(0)
        return pop_value

    def show_value(self):
        """Фунция показа содержимого буфера"""

        return self.buffer

    def is_empty(self):
        """Функция очистки буфера"""

        self.buffer = []
