# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# import requests
# import bs4
# import pytest
from practice_c1.myclass import MyClass
import sys
print(sys.path)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm. Wow!')

if __name__ == "__main__":
    m = MyClass()
    print("It's really working:", m.f())


def rec_reverse(str_):
    str_length = len(str_)
    if str_length <= 1:
        return str_
    return str_[str_length - 1] + rec_reverse(str_[:str_length - 1])


def rec_digits_sum(number):
    if number < 10:
        return number
    return number % 10 + rec_digits_sum(number // 10)


def get_naturals(start=1, step=1):
    number = start
    while True:
        yield number
        number += step


'''import time


def decorator_time(fn):
    def wrapper():
        print(f"Запустилась функция {fn}")
        t0 = time.time()
        for _ in range(100):
            result = fn()
        dt = time.time() - t0
        print(f"Функция выполнилась 100 раз. Время: {dt:.10f}")
        return dt  # задекорированная функция будет возвращать время работы
    return wrapper


def pow_2():
    return 10000000 ** 2


def in_build_pow():
    return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
in_build_pow()'''

'''def count_usage(fn):
    fn_counter = 0

    def wrapper(*args, **kwargs):
        nonlocal fn_counter
        fn(*args, **kwargs)
        fn_counter += 1
        print(f"Функция {fn} выполнилась уже {fn_counter} раз.")

    return wrapper


@count_usage
def new_print(text):
    print(text)


new_print('Hello!')
new_print('Hello!')'''


def add_cache(func):
    results = dict()

    def wrapper(number):
        nonlocal results
        if number not in results:
            results[number] = func(number)
            print(f'Result {results[number]} was added to cache.')
        else:
            print(f'Result {results[number]} was taken from cache')
        print(f'Cache: {results}')
        return results[number]

    return wrapper


@add_cache
def f(n):
    return n * 123456789


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def quadratic_solve(a, b, c):
    dnt = discriminant(a, b, c)
    if dnt < 0:
        return "Нет вещественных корней"
    elif dnt == 0:
        return -b / (2 * a)
    else:
        return (-b - dnt ** 0.5) / (2 * a), (-b + dnt ** 0.5) / (2 * a)


def rec_min(ls):
    if len(ls) == 1:
        return ls[0]
    if ls[0] <= rec_min(ls[1:]):
        return ls[0]
    else:
        return rec_min(ls[1:])


def rec_reverse2(a):
    s = str(a)
    if len(s) == 1:
        return s[0]
    return rec_reverse2(int(s[1:])) + s[0]


def mirror(a, res=0):
    return mirror(a // 10, res * 10 + a % 10) if a else res


def equal(n, s):
    if s < 0:
        return False
    if n < 10:
        return n == s
    else:
        return equal(n // 10, s - n % 10)


'''
def e():
    n = 1
    while True:
        yield (1 + 1/n) ** n
        n += 1


last = 0
for a in e():  # e() - генератор
    if (a - last) < 0.00000001:  # ограничение на точность
        print(a)
        break  # после достижения которого завершаем цикл
    else:
        last = a  # иначе - присваиваем новое значение


def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")
    return wrapper


def has_access(func):
    def wrapper():
        if username in USERS:
            print("Пользователь имеет доступ к базе данных")
            func()
        else:
            print("Пользователь не имеет доступа к базе. Соединение завершено.")
    return wrapper


USERS = ['admin', 'guest', 'director', 'root', 'superstar']

# yesno = input("""Введите Y, если хотите авторизоваться, или N,
#             если хотите продолжить работу как анонимный пользователь: """)

# auth = yesno == "Y"

# if auth:
#    username = input("Введите ваш username:")


@is_auth
@has_access
def from_db():
    print("some data from database")


# from_db()'''
