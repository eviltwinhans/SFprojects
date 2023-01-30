from contextlib import contextmanager


"""
Напишите контекстный менеджер, который умеет безопасно работать с файлами.
В конструктор объекта контекстного менеджера передаются два аргумента:
первый — путь к файлу, который надо открыть,
второй — тип открываемого файла (для записи, для чтения и т. д.).

При входе в контекстный менеджер должен открываться файл, и возвращаться объект для работы с этим файлом.
При выходе из контекстного менеджера файл должен закрываться.
Эталоном работы можно считать контекстный менеджер open.
"""


class FileEditor:
    def __init__(self, path, mode):
        self.file = open(path, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager  # оборачиваем функцию в декоратор contextmanager
def file_editor(path, mode):
    file = open(path, mode)
    yield file
    file.close()


with FileEditor('scores.txt', 'a') as f:
    f.write("\nMy own context manager works!")

with file_editor('scores.txt', 'a') as f:
    f.write("\nThis context manager works too!")
