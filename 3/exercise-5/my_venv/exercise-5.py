# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''

from random import randint

my_list = [randint(-10,10) for _ in range(10)]
print(f'Список: {my_list}')

index = -1
for i in range(0, len(my_list)):
    if my_list[i] < 0 and index == -1:
        index = i
    elif (my_list[i] < 0) and (my_list[i] > my_list[index]):
        index = i
print(f'Максимальный отрицательный элемент в списке: {my_list[index]} имеет индекс: {index}')
