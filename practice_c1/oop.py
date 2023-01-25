from math import pi


class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Метод, рассчитывающий площадь
    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return True if (self.width == other.width and self.height == other.height) \
                       or (self.width == other.height and self.height == other.width) else False

    def __str__(self):
        return f'Rectangle: {self.x, self.y, self.width, self.height}'


class Square:
    _side = None

    def __init__(self, a):
        self.side = a

    @property
    def get_area_square(self):
        return self._side ** 2

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
        else:
            raise ValueError("Square side should be a positive number")


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return pi * (self.r ** 2)


class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance}.'

    def show_client(self):
        print(f'{self.name} {self.surname} is from {self.city}.')


class SquareFactory:

    @staticmethod
    def init_square(a):
        return Square(a)


# square_1 = SquareFactory.init_square(1)
# print(square_1.a)
