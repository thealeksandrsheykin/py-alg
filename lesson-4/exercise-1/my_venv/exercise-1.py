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
from timeit import timeit

# 1. Находим сумму с помощью одного цикла

def my_func_1(n):
    my_var = 0
    my_data = 1
    for i in range(n):
        #print(f'{my_data}', sep=';', end=' ')
        my_var += my_data
        my_data /= -2
    return my_var

def my_func_main():
    global n
    my_func_1(n)

print(f'Первый способ:\n')
for n in (10,100,1000,10000,100000):
    print(f'Время выполнения при "n" = {n} (timeit):'
          f' {timeit(stmt="my_func_1(n)",setup="from __main__ import my_func_1, n",number=1000)}')
    cProfile.run("my_func_main()")

# timeit my_func_1(10)      : 0.0010532999995120917
# timeit my_func_1(100)     : 0.007337500000176078
# timeit my_func_1(1000)    : 0.08053979999931471
# timeit my_func_1(10000)   : 0.8545848000003389
# timeit my_func_1(100000)  : 8.736562499999309

# cProfile my_func_1(10)    : 1    0.000    0.000    0.000    0.000 exercise-1.py:18(my_func_1)
# cProfile my_func_1(100)   : 1    0.000    0.000    0.000    0.000 exercise-1.py:18(my_func_1)
# cProfile my_func_1(1000)  : 1    0.000    0.000    0.000    0.000 exercise-1.py:18(my_func_1)
# cProfile my_func_1(10000) : 1    0.001    0.001    0.001    0.001 exercise-1.py:18(my_func_1)
# cProfile my_func_1(100000): 1    0.009    0.009    0.009    0.009 exercise-1.py:18(my_func_1)

def my_func_2(n,data=1,res=0):
    if n > 0:
        res += data
        return my_func_2(n-1,data/-2,res)
    else:
        return res

def my_func_main():
    global n
    my_func_2(n)

print(f'Второй способ:\n')
for n in (10,100,1000,10000,100000):
    print(f'Время выполнения при "n" = {n} (timeit):'
          f' {timeit(stmt="my_func_2(n)",setup="from __main__ import my_func_2, n",number=1000)}')
    cProfile.run("my_func_main()")

# timeit my_func_2(10)      : 0.002122599999893282
# timeit my_func_2(100)     : 0.02089330000035261
# timeit my_func_2(1000)    : maximum recursion depth exceeded in comparison
# timeit my_func_2(10000)   : maximum recursion depth exceeded in comparison
# timeit my_func_2(100000)  : maximum recursion depth exceeded in comparison

# cProfile my_func_2(10)    : 11/1     0.000    0.000    0.000    0.000 exercise-1.py:50(my_func_2)
# cProfile my_func_2(100)   : 101/1    0.000    0.000    0.000    0.000 exercise-1.py:50(my_func_2)
# cProfile my_func_2(1000)  : maximum recursion depth exceeded in comparison
# cProfile my_func_2(10000) : maximum recursion depth exceeded in comparison
# cProfile my_func_2(100000): maximum recursion depth exceeded in comparison
