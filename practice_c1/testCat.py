from cats import Cat


mu = Cat('Mu', 'girl', 3)

print(mu.get_name())
print(mu.get_sex())
print(mu.get_age())

"""Создайте класс Dog с помощью наследования класса Cat.
Создайте метод get_pet() таким образом, чтобы он возвращал только имя и возраст.
Далее сделайте вывод этой информации в консоль.
"""


class Dog(Cat):
    def get_pet(self):
        return self.name + ', ' + str(self.age)


frank = Dog('Frank', 'boy', 2)

print(frank.get_pet())
