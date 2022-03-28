# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50]. Выведите на экран исходный и отсортированный массивы.
'''

from random import randrange
from timeit import timeit

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result

def merge_sort(array):
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    return merge(left,right)

if __name__ == '__main__':
    my_list = [None] * 10
    for i in range(len(my_list)):
        my_list[i] = randrange(0,50)
    print(f'Исходный массив: {my_list}\n'
          f'Отсортированный массив: {merge_sort(my_list)}\n'
          f'''Время выполнения: {timeit(stmt="merge_sort(my_list)",
                                        setup="from __main__ import merge_sort, my_list",
                                        number=1000)} мс''')


