try:
    value = int(input('Введите число:\t'))
except ValueError as e:
    print(e, '\nВы ввели неправильное число')
else:
    print(f'Вы ввели {value}')
finally:
    print('Выход из программы')
