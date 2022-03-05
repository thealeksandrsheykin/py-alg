# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
и максимальный элементы в сумму не включать.
'''

from random import randint

my_list = [randint(1, 100) for _ in range(10)]
print(f'Список: {my_list}')

if my_list.index(min(my_list)) < my_list.index(max(my_list)):
    a = my_list.index(min(my_list)) + 1
    b = my_list.index(max(my_list))
else:
    a = my_list.index(max(my_list)) + 1
    b = my_list.index(min(my_list))

print(f'Элементы находящиеся между минимальным и максимальнм элементами: {sum(my_list[a:b])}')

