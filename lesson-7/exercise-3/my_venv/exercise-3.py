# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
3.Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой на-
зывается элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой
– не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте
метод сортировки, который не рассматривался на уроках.
'''
from random import randrange,choice
from statistics import median
from timeit import timeit

def my_func_1(array):
    return median(array)

# ----------------------------------------------#

def my_func_2(array):
    array.sort()
    middle = len(array) // 2
    return (array[middle] + array[middle]) / 2

# ----------------------------------------------#

def my_func_3(array,pivot_func = choice):
    if len(array) % 2 == 1:
        return my_func_31(array, len(array)/2, pivot_func)
    else:
        return 0.5 * (my_func_31(array, len(array)/2-1,pivot_func) +
                      my_func_31(array, len(array)/2, pivot_func))

def my_func_31(array,idx,pivot_func):
    if len(array) == 1:
        return array[0]
    pivot = pivot_func(array)
    l_list = [i for i in array if i <  pivot]
    r_list = [i for i in array if i >  pivot]
    p_list = [i for i in array if i == pivot]
    if idx < len(l_list):
        return my_func_31(l_list,idx,pivot_func)
    elif idx < len(l_list) + len(p_list):
        return p_list[0]
    else:
        return my_func_31(r_list, idx - len(l_list) - len(p_list), pivot_func)


if __name__ == '__main__':
    m = 4
    size = (2 * m) + 1
    my_list = [None] * size
    for i in range(len(my_list)):
        my_list[i] = randrange(-100,100)
    print(f'Исходный массив: {my_list}\n'
          f'Медиана(Способ №1): {my_func_1(my_list)}\n'
          f'''Время выполнения: {timeit(stmt="my_func_1(my_list)",
                                        setup="from __main__ import my_func_1, my_list",
                                        number=1000)} мс\n'''
          f'Медиана(Способ №2): {my_func_2(my_list)}\n'
          f'''Время выполнения: {timeit(stmt="my_func_2(my_list)",
                                        setup="from __main__ import my_func_2, my_list",
                                        number=1000)} мс\n'''
          f'Медиана(Способ №3): {my_func_3(my_list)}\n'
          f'''Время выполнения: {timeit(stmt="my_func_3(my_list)",
                                        setup="from __main__ import my_func_3, my_list",
                                        number=1000)} мс''')
