# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
1.Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По
возможности доработайте алгоритм (сделайте его умнее).
'''
from random import randrange
from timeit import timeit


def bubble_sort_1(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def bubble_sort_2(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i+ 1], array[i]
                swapped = True
    return array

def bubble_sort_3(array):
    swapped = False
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


if __name__== '__main__':
    my_list = [None] * 10
    for i in range(len(my_list)):
        my_list[i] = randrange(-100, 100)

    print(f'Исходный список: {my_list}\n')
    array_1 = my_list.copy()
    print(f'Отсортированный список(Cпособ №1): {bubble_sort_1(array_1)}\n'
          f'''Время выполнения: {timeit(stmt="bubble_sort_1(array_1)",
                                        setup="from __main__ import bubble_sort_1, array_1",
                                        number=1000):.8f} мс''')
    array_2 = my_list.copy()
    print(f'Отсортированный список(Cпособ №2): {bubble_sort_2(array_2)}\n'
          f'''Время выполнения: {timeit(stmt="bubble_sort_2(array_2)",
                                        setup="from __main__ import bubble_sort_2, array_2",
                                        number=1000):.8f} мс''')
    array_3 = my_list.copy()
    print(f'Отсортированный список(Cпособ №3): {bubble_sort_3(array_3)}\n'
          f'''Время выполнения: {timeit(stmt="bubble_sort_3(array_3)",
                                        setup="from __main__ import bubble_sort_3, array_3",
                                        number=1000):.8f} мс''')


