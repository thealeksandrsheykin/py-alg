# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''
from random import randint

my_list = [[randint(1,20) for i in range(0,5)] for j in range(0,4)]
for i in my_list:
    print(i)

my_var_1 = 0
for j in range(0,5):
    my_var_2 = 21
    for i in range(0,4):
        if my_list[i][j] < my_var_2:
            my_var_2 = my_list[i][j]
        else: continue
    if my_var_2 > my_var_1:
        my_var_1 = my_var_2

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {my_var_1}')

