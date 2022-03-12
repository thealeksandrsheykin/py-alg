# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
являться минимальными), так и различаться.
'''

from random import randint

# 1.Cпособ
my_list = [randint(1, 100) for _ in range(10)]
print(f'Список: {my_list}')

min_1 = min(my_list)
my_list.remove(min_1)
min_2 = min(my_list)
print(f'Два наименьших элемента: {min_1,min_2}')

# 2.Способ
my_list = [randint(1, 100) for _ in range(10)]
print(f'Список: {my_list}')

min_1 = 0
min_2 = 1
for i in range(2, len(my_list)):
    if my_list[min_1] > my_list[i]:
        if my_list[min_1] < my_list[min_2]:
            min_2 = min_1
        min_1 = i
    elif my_list[i] < my_list[min_2]:
        min_2 = i
print(f'Два наименьших элемента: {my_list[min_1],my_list[min_2]}')






