# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2.Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15,
6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
'''
from random import randint
my_list_1 = list()
my_list_2 = list()

my_list_1 = [randint(1,100) for i in range(10)]
print(f'Первый массив: {my_list_1}')

# 1.Способ
for i in range(0,len(my_list_1)-1):
    if i % 2 == 0:
        my_list_2.append(my_list_1[i])
    else: continue
print(f'1.Cпособ:\n'
      f'Второй массив: {my_list_2}')


# 2.Способ
start = 0
my_list_2 = list()
for i in my_list_1:
    index = my_list_1.index(i,start)
    start += 1
    if index % 2 == 0:
        my_list_2.append(i)
    else: continue
print(f'2.Cпособ:\n'
      f'Второй массив: {my_list_2}')

