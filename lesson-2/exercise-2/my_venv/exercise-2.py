# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2.Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''
# 1. Рекурсия
def my_func(data, even=0, odd=0):
    if data:
        if data % 2 == 0:
            even += 1
            return my_func(data//10,even,odd)
        else:
            odd += 1
            return my_func(data//10,even,odd)
    else:
        print(f'Четных:   {even}\n'
              f'Нечетных: {odd}\n')

print(f'1.Cпособ(Рекурсия):\n')
data = int(input('Введите число: '))
my_func(data)

# 2.Цикл

even = 0
odd  = 0
while data:
    if data % 2 == 0:
        even += 1
    else:
        odd += 1
    data = data // 10

print(f'2.Cпособ(Цикл):\n')
print(f'Четных:   {even}\n'
      f'Нечетных: {odd}\n')

