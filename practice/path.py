import os


start_path = os.getcwd()
print(start_path)

os.chdir("..")  # подняться на один уровень выше
print(os.getcwd())

os.chdir(start_path)
print(os.getcwd())

print(os.listdir())

if 'oop.py' not in os.listdir():
    print("Файл отсутствует в данной директории")

print(start_path)
print(os.path.join(start_path, 'test'))

"""
Сделайте функцию, которая принимает от пользователя путь
и выводит всю информацию о содержимом этой папки.
Для реализации используйте функцию встроенного модуля os.walk().
Если путь не указан, то сравнение начинается с текущей директории.
"""


def get_context(path=os.getcwd()):
    return os.walk(path)


# print(*get_context(), sep="\n")


def walk_desc(path=None):
    start = path if path is not None else os.getcwd()

    for root, dirs, files in os.walk(start):
        print("Текущая директория", root)
        print("---")

        if dirs:
            print("Список папок", dirs)
        else:
            print("Папок нет")
        print("---")

        if files:
            print("Список файлов", files)
        else:
            print("Файлов нет")
        print("---")

        if files and dirs:
            print("Все пути:")
        for f in files:
            print("Файл ", os.path.join(root, f))
        for d in dirs:
            print("Папка ", os.path.join(root, d))
        print("===")


# walk_desc()

f = open('test.txt', 'w', encoding='utf8')

# Запишем в файл 2 строки
f.write("This is a test string\n")
f.write("This is a new string\n")
f.close()

f = open('test.txt', 'r', encoding='utf8')
print(f.read(10))
print(f.read())
f.close()

f = open('test.txt', 'a', encoding='utf8')  # открываем файл на дозапись
sequence = ["other string\n", "123\n", "test test\n"]
f.writelines(sequence)  # берёт строки из sequence и записывает в файл (без переносов)
f.close()

# Попробуем теперь построчно считать файл с помощью readlines:
f = open('test.txt', 'r', encoding='utf8')
print(f.readlines())  # считывает все строки в список и возвращает список
f.close()

f = open('test.txt', 'r', encoding='utf8')
print(f.readline())  # This is a test string
print(f.read(4))  # This
print(f.readline())  # is a new string
f.close()
