"""
Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.
"""

try:
    f = open('input.txt', 'x', encoding='utf8')
    sequence = ["other string\n", "123\n", "test test\n"]
    f.writelines(sequence)
    f.close()
except Exception:
    print("File has been already initiated.")

with open("input.txt", 'r') as source:
    text = source.readlines()

backup = open('output.txt', 'w', encoding='utf8')
backup.writelines(text)
backup.close()

# with open('input.txt', 'r') as input_file:
#     with open('output.txt', 'w') as output_file:
#         for line in input_file:
#             output_file.write(line)

"""
Дан файл numbers.txt, компоненты которого являются действительными числами
(файл создайте самостоятельно и заполните любыми числами, в одной строке одно число).
Найдите сумму наибольшего и наименьшего из значений и запишите результат в файл output.txt.
"""

file = open('numbers.txt', 'r')  # можно перечислять строки в файле
lines = file.readlines()
numbers = []
for line in lines:
    numbers.append(int(line.strip()))

min_number = min(numbers)
max_number = max(numbers)

with open('output.txt', 'a') as out:
    out.write('\n')
    out.write(str(min_number + max_number))

# filename = 'numbers.txt'
# output = 'output.txt'
#
# with open(filename) as f:
#    min_ = max_ = float(f.readline())  # считали первое число
#    for line in f:
#        num =  float(line)
#        if num > max_:
#            max_ = num
#        elif num < min_:
#            min_ = num
#
#    sum_ = min_ + max_
#
# with open(output, 'w') as f:
#    f.write(str(sum_))
#    f.write('\n')

"""
В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную.
Выведите на экран всех учащихся, чья оценка меньше 3 баллов.
"""

data = open('scores.txt', 'r')
for line in data:
    if int(line.strip()[-1]) < 3:
        print(line, end='')
data.close()

# with open('input.txt', encoding="utf8") as file:
#     for line in file:
#         points = int(line.split()[-1])
#         if points < 3:
#             name = " ".join(line.split()[:-1])
#             print(name)

"""
Выполните реверсирование строк файла (перестановка строк файла в обратном порядке).
"""
with open('scores.txt', 'r') as file:
    data = file.readlines()[::-1]

with open('scores.txt', 'w') as file:
    file.writelines(data)

# with open('input.txt', 'r') as input_file:
#     with open('output.txt', 'w') as output_file:
#         for line in reversed(input_file.readlines()):
#             output_file.write(line)

