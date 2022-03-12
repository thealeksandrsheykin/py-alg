# -*-coding: utf-8 -*-
# !/usr/bin/env python3

'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
'''

import cProfile
from timeit import timeit

# Решето Эратосфена
'''
Это алгоритм нахождения простых чисел до заданного числа N. При его выполнении последовательно отделяются
составные числа, кратные простым, начиная с 2.
'''


def my_func_1(n):
    my_list = [i for i in range(n)]
    my_list[1] = 0
    m = 2
    while m < n:
        if my_list[m] != 0:
            j = m * 2
            while j < n:
                my_list[j] = 0
                j = j + m
        m += 1
    return [i for i in my_list if i != 0]

def my_func_main():
    global n
    my_func_1(n)

print(f'Первый способ:\n')
for n in (10,100,1000,10000,100000):
    print(f'Время выполнения при "n" = {n} (timeit):'
          f' {timeit(stmt="my_func_1(n)",setup="from __main__ import my_func_1, n",number=1000)}')
    cProfile.run("my_func_main()")

# timeit my_func_1(10)      : 0.0027649000003293622
# timeit my_func_1(100)     : 0.027418400000897236
# timeit my_func_1(1000)    : 0.32188639999912994
# timeit my_func_1(10000)   : 3.5902828999987833
# timeit my_func_1(100000)  : 40.40777259999959

# cProfile my_func_1(10)    : 1    0.000    0.000    0.000    0.000 exercise-2.py:17(my_func_1)
# cProfile my_func_1(100)   : 1    0.000    0.000    0.000    0.000 exercise-2.py:17(my_func_1)
# cProfile my_func_1(1000)  : 1    0.000    0.000    0.000    0.000 exercise-2.py:17(my_func_1)
# cProfile my_func_1(10000) : 1    0.003    0.003    0.004    0.004 exercise-2.py:17(my_func_1)
# cProfile my_func_1(100000): 1    0.032    0.032    0.039    0.039 exercise-2.py:17(my_func_1)

def my_func_2(n):
    my_list = list()
    for i in range(2, n+1):
        my_var = 0
        for j in range(1,i+1):
            if i % j == 0:
                my_var += 1
            elif my_var > 2:
                break
        if my_var == 2:
            my_list.append(i)
    return my_list

def my_func_main():
    global n
    my_func_2(n)

print(f'Второй способ:\n')
for n in (10,100,1000,10000,100000):
    print(f'Время выполнения при "n" = {n} (timeit):'
          f' {timeit(stmt="my_func_2(n)",setup="from __main__ import my_func_2, n",number=1000)}')
    cProfile.run("my_func_main()")

# timeit my_func_2(10)      : 0.006684699999823351
# timeit my_func_2(100)     : 0.2274823000007018
# timeit my_func_2(1000)    : 11.307372400000531
# timeit my_func_2(10000)   :
# timeit my_func_2(100000)  :

# cProfile my_func_2(10)    : 1    0.000    0.000    0.000    0.000 exercise-2.py:53(my_func_2)
# cProfile my_func_2(100)   : 1    0.000    0.000    0.000    0.000 exercise-2.py:53(my_func_2)
# cProfile my_func_2(1000)  : 1    0.011    0.011    0.011    0.011 exercise-2.py:53(my_func_2)
# cProfile my_func_2(10000) :
# cProfile my_func_2(100000):


def my_func_3(n):
    my_list = [2]
    for i in range(3,n+1):
        my_var = True
        for j in my_list:
            if i % j == 0:
                my_var = False
                break
        if my_var:
            my_list.append(i)
    return my_list

def my_func_main():
    global n
    my_func_3(n)

print(f'Третий способ:\n')
for n in (10,100,1000,10000,100000):
    print(f'Время выполнения при "n" = {n} (timeit):'
          f' {timeit(stmt="my_func_3(n)",setup="from __main__ import my_func_3, n",number=1000)}')
    cProfile.run("my_func_main()")

# timeit my_func_3(10)      : 0.001645000000280561
# timeit my_func_3(100)     : 0.053433000000950415
# timeit my_func_3(1000)    : 0.9637888999986899
# timeit my_func_3(10000)   : 50.03988559999925
# timeit my_func_3(100000)  :

# cProfile my_func_3(10)    : 1    0.000    0.000    0.000    0.000 exercise-2.py:89(my_func_3)
# cProfile my_func_3(100)   : 1    0.000    0.000    0.000    0.000 exercise-2.py:89(my_func_3)
# cProfile my_func_3(1000)  : 1    0.001    0.001    0.001    0.001 exercise-2.py:89(my_func_3)
# cProfile my_func_3(10000) : 1    0.047    0.047    0.047    0.047 exercise-2.py:89(my_func_3)
# cProfile my_func_3(100000): 