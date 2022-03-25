# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
1.Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''

# Python: python 3.9.5
# OS: Windows 10 21H1 x64 сборка: 19043.1586

from sys import getsizeof

#Lesson-3
'''
2.Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15,
6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
'''

from random import randint

# 1.Способ
my_list_1 = list()
my_list_2 = list()

print('Объявление массивов:')
print(f'Массив "MY_LIST_1" занимает: {getsizeof(my_list_1)} Byte')
print(f'Массив "MY_LIST_2" занимает: {getsizeof(my_list_2)} Byte')
print('-' * 24)

my_list_1 = [randint(1,100) for i in range(10)]
print(f'\nПервый массив: {my_list_1}')
print(f'Массив "MY_LIST_1" c  10  элементами занимает: {getsizeof(my_list_1)} Byte')
print('-' * 24)

for i in range(0,len(my_list_1)-1):
    if i % 2 == 0:
        my_list_2.append(my_list_1[i])
        print(f'Второй массив: {my_list_2}')
        print(f'Массив "MY_LIST_2" c добавленым новым элементом занимает: {getsizeof(my_list_2)} Byte')
        print('-' * 24)
    else: continue
print(f'1.Cпособ:\n'
      f'Второй массив: {my_list_2}')

# Пустой массив my_list_1 = 56 Byte
# Пустой массив my_list_2 = 56 Byte

# Массив my_list_1 c 10 элементами = 184 Byte => 56 Byte + (12.8 Byte * 10)
#--------------------------------------------------------------------------#
# Массив my_list_2 c 1 элементом   = 88  Byte => 56 Byte + 32 Byte
# Массив my_list_2 c 2 элементами  = 88  Byte => 56 Byte + (16 Byte * 2)
# Массив my_list_2 c 3 элементами  = 88  Byte => 56 Byte + (10.6 Byte * 3)
# Массив my_list_2 c 4 элементами  = 88  Byte => 56 Byte + (8 Byte * 4)
# Массив my_list_2 c 5 элементами  = 120 Byte => 56 Byte + (12.8 Byte * 5)
#--------------------------------------------------------------------------#


# 2.Способ
my_list_1 = [None] * 10
my_list_2 = [None] * 5

print('Объявление массивов:')
print(f'Массив "MY_LIST_1" занимает: {getsizeof(my_list_1)} Byte')
print(f'Массив "MY_LIST_2" занимает: {getsizeof(my_list_2)} Byte')
print('-' * 24)

for i in range(10):
    my_list_1[i] = randint(1,100)

print(f'\nПервый массив: {my_list_1}')
print(f'Массив "MY_LIST_1" c  10  элементами занимает: {getsizeof(my_list_1)} Byte')
print('-' * 24)

index = 0
for i in range(0,len(my_list_1)-1):
    if i % 2 == 0:
        my_list_2[index] = my_list_1[i]
        index += 1
        print(f'Второй массив: {my_list_2}')
        print(f'Массив "MY_LIST_2" c добавленым новым элементом занимает: {getsizeof(my_list_2)} Byte')
        print('-' * 24)
    else: continue
print(f'2.Cпособ:\n'
      f'Второй массив: {my_list_2}')

# Пустой массив my_list_1 = 136 Byte
# Пустой массив my_list_2 = 96 Byte

# Массив my_list_1 c 10 элементами = 136 Byte => 56 Byte + (8 Byte * 10)
#--------------------------------------------------------------------------#
# Массив my_list_2 c 1 элементом   = 96 Byte => 56 Byte + 40 Byte
# Массив my_list_2 c 2 элементами  = 96 Byte => 56 Byte + (20 Byte * 2)
# Массив my_list_2 c 3 элементами  = 96 Byte => 56 Byte + (13.3 Byte * 3)
# Массив my_list_2 c 4 элементами  = 96 Byte => 56 Byte + (10 Byte * 4)
# Массив my_list_2 c 5 элементами  = 96 Byte => 56 Byte + (8 Byte * 5)
#--------------------------------------------------------------------------#
