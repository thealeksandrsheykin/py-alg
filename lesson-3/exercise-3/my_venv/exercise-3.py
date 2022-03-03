# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint

my_list = [randint(1,100) for i in range (10)]

# 1. Способ
print(f'Массив: {my_list}')
a = max(my_list)
b = min(my_list)
print(f'Max: {a}\n'
      f'Min: {b}')
index_a = my_list.index(a)
index_b = my_list.index(b)
my_list[index_a],my_list[index_b] = my_list[index_b],my_list[index_a]
print(f'Измененный массив: {my_list}')

# 2. Cпособ
index_a, index_b = [ i (range(len(my_list)), key=my_list.__getitem__) for i in [min, max]]
my_list[index_a],my_list[index_b] = my_list[index_b],my_list[index_a]
print(f'Измененный массив: {my_list}')

# 3. Способ
a = my_list[0]
b = my_list[0]
for i in range(0,len(my_list)-1):
      if my_list[i] > a:
            a = my_list[i]
            index_a = i
      elif my_list[i] < b:
            b = my_list[i]
            index_b = i
my_list[index_a],my_list[index_b] = my_list[index_b],my_list[index_a]
print(f'Измененный массив: {my_list}')
