# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, то надо вывести число 6843.
'''
data = int(input('Введите число: '))
# 1. Способ
# data [::-1]

# 2. Способ
result = 0
while data:
    result = result * 10 + (data % 10)
    data = data // 10

print(f'Наоборот: {result}')

# 3.Способ
result = 0
def my_func(data):
    global result
    if data:
        result = result * 10 + (data % 10)
        my_func(data // 10)
    return result


data = int(input('Введите число: '))
print(f'Наоборот: {my_func(data)}')