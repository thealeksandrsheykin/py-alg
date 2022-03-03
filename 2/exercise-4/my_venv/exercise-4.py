# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
'''
# 1. Способ
n = int(input('Введите кол-во элементов: '))
sum  = 0
data = 1

for i in range(n):
    print(f'{data}', sep=';', end = ' ')
    sum += data
    data /= -2
print(f'\n{sum}')

# 2. Cпособ
def my_func(n,data=1,sum=0):
    if n > 0:
        sum += data
        return my_func(n-1,data/-2,sum )
    else:
        return sum

n = int(input('Введите кол-во элементов: '))
print(my_func(n))



