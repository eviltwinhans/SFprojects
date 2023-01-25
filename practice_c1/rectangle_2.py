from oop import Rectangle, Square, Client


# далее создаём два прямоугольника
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
# вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

rect_3 = Rectangle(5, 12)
rect_4 = Rectangle(12, 5, -1, -1)
print(rect_1 == rect_2)
print(rect_4 == rect_2)
print(rect_3 == rect_2)

print(rect_4)
print(rect_4.get_area())

client_1 = Client('Artur', 'Kane', 'Glasgow', 100500)
client_2 = Client('Miles', 'McGrow', 'Toronto', 200500)

for client in [client_1, client_2]:
    client.show_client()
