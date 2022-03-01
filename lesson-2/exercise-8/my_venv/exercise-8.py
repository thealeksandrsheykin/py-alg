# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
и цифра, которую необходимо посчитать, задаются вводом с клавиатуры
'''

n = int(input('Введите кол-во вводимых чисел: '))
number = int(input('Введите цифру: '))

# 1. Способ
for i in range(0, n):
    cnt = 0
    data = int(input(f'Введите число №{i + 1}: '))
    tmp_data = data
    while tmp_data:
        if tmp_data % 10 == number:
            cnt += 1
        tmp_data = tmp_data // 10
    print(f'Цифра {number} встречается в {data}: {cnt}')

# 2. Способ
def my_func(number, data):
    if not data:
        return 0
    elif number == data % 10:
        return 1 + my_func(number, data // 10)
    else:
        return 0 + my_func(number, data // 10)


n = int(input('Введите кол-во вводимых чисел: '))
number = int(input('Введите цифру: '))

for i in range(n):
    data = int(input(f'Введите число №{i + 1}: '))
    print(f'Цифра {number} встречается в {data}: {my_func(number, data)}')


