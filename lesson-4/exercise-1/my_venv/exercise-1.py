# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех
уроков.
'''

'''
Задание №2.4
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... Количество элементов (n) вводится с клавиатуры.
'''
import cProfile
from timeit import timeit, Timer

# 1. Находим сумму с помощью одного цикла

my_code_1 = '''
def my_func_1():
    my_var = 0
    my_data = 1
    for i in range(10):
        print(f'{my_data}', sep=';', end=' ')
        my_var += my_data
        my_data /= -2
    return my_var
'''


def my_func_1():
    my_var = 0
    my_data = 1
    for i in range(10):
        print(f'{my_data}', sep=';', end=' ')
        my_var += my_data
        my_data /= -2
    return my_var


# 2. Находим сумму с помощью рекурсии
my_code_2 = '''
def my_func_2(n, my_var_1=1, my_var_2=0):
    if n > 0:
        my_var_2 += data
        return my_func_2(n - 1, my_var_1 / -2, my_var_2)
    else:
        return my_var_2
'''


def my_func_2(n, my_var_1=1, my_var_2=0):
    if n > 0:
        my_var_2 += my_var_1
        return my_func_2(n - 1, my_var_1 / -2, my_var_2)
    else:
        return my_var_2


if __name__ == '__main__':
    # Первый способ:
   # print(timeit(stmt=my_code_1, number=10000))
   # cProfile.run("my_func_1()")
    # Второй способ:
    t = Timer(my_func_2(10))
    t.timeit(5)
   # cProfile.run("my_func_2()")
