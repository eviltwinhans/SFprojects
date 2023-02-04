"""
С помощью стека проверять баланс только круглых скобок может показаться слишком затратным.
И это действительно так.
Однако написанную нами функцию можно расширить для проверки баланса скобок разного рода:
круглых, квадратных и фигурных, например.

Модифицируйте функцию проверки баланса скобок для двух видов скобок: круглых и квадратных.

Для реализации такого алгоритма может быть полезным создание словаря,
в котором закрывающая скобка — ключ, открывающая — значение.
"""


def bracket_checker(text):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for letter in text:
        if letter in pairs.keys():
            stack.append(letter)
        elif letter in pairs.values():
            if len(stack) > 0 and pairs[stack[-1]] == letter:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(bracket_checker(')(vvb[ccc(aaa)mm] n n {}ccc)'))


# Создадим класс Queue — нужная нам очередь
class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди

    def is_empty(self):  # очередь пуста?
        # да, если указатели совпадают и в ячейке нет задачи
        return self.head == self.tail and self.tasks[self.head] == 0

    # Добавьте в класс Queue метод size, который возвращает текущий размер очереди.
    # Учтите, что необходимо рассмотреть несколько случаев: когда очередь пустая,
    # когда очередь полная (какому условию соответствует?),
    # а также отдельное внимание стоит обратить на тот случай,
    # когда хвост очереди переместился в начало списка (закольцевался).
    def size(self):
        if self.is_empty():
            return 0
        elif self.head == self.tail:
            return self.max_size
        elif self.head < self.tail:
            return self.tail - self.head
        else:
            return self.max_size + self.tail - self.head

    # Добавьте в класс Queue метод add, который добавляет задачу в конец очереди.
    # Также учтите, что размер массива ограничен и при достижении этого предела,
    # необходимо перенести указатель в положение 0.
    # После добавления задачи в очередь, она должна вывести уведомление об этом в формате:
    # "Задача №1 добавлена"
    def add(self):
        self.task_num += 1
        self.tasks[self.tail] = self.task_num
        self.tail = (self.tail + 1) % self.max_size
        print(f"Task #{self.task_num} has been added.")
        return None

    # Добавьте в класс Queue метод show, печатающий информацию о приоритетной задаче в формате
    # "Задача №1 в приоритете"
    def show(self):
        print(f"Task #{self.tasks[self.head]} is the highest priority.")

    # Добавьте в класс Queue метод do, которая печатает в консоль задачу (= выполняет ее) и,
    # соответственно, удаляет ее из очереди, присваивая ей значение 0. Формат вывода:
    # "Задача №1 выполнена"
    def do(self):
        print(f"Task #{self.tasks[self.head]} has been done.")
        self.tasks[self.head] = 0
        self.head = (self.head + 1) % self.max_size


# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add":
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")
