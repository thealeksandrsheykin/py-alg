# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2.Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50]. Выведите на экран исходный и отсортированный массивы.
'''

from random import randrange

def merge(left,right):
    result = list()
    l_idx = r_idx = 0
    for i in range(len(left) + len(right)):
        if l_idx < len(left) and r_idx < len(right):
            if left[l_idx] <= right[r_idx]: # Сравниваем первые элементы в начале каждого списка. Если первый элемент
                result.append(left[l_idx])  # левого списка меньше, добавляем его в результат
                l_idx += 1
            else:
                result.append(right[r_idx]) # Иначе добавляем первый элемент правого списка в результат
                r_idx += 1
        elif l_idx == len(left):            # Проверяем конец левого списка, элементы правого списка добавляем в
            result.append(right[r_idx])     # в результат
            r_idx += 1
        elif r_idx == len(right):           # Проверяем конец правого списка, элементы левого списка добавляем в
            result.append(left[l_idx])      # результат
            l_idx += 1
    return result


def merge_sort(array):
    if len(array) <= 1:                     # Если список состоит из одного элемента, то возвращаем его
        return array
    else:
        middle = len(array) // 2            # Находим середину списка
        left = merge_sort(array[:middle])   # Делим левый список
        right = merge_sort(array [middle:]) # Делим правый список
    print('L:', left, 'R:', right)
    return merge(left,right)                # Объединяем отсортированные списки



if __name__ == '__main__':
    my_list = [None] * 10
    for i in range(len(my_list)):
        my_list[i] = randrange(0,50)
    print(f'Исходный массив: {my_list}\n'
          f'Отсортированный массив: {merge_sort(my_list)}')






