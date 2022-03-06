# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных
элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''

my_list = list()

for i in range(0,5):
    summa = 0
    tmp_list = list()
    for j in range(0,3):
        my_var = int(input(f'Введите значение {i+1,j+1}: '))
        tmp_list.append(my_var)
        summa += my_var
    tmp_list.append(summa)
    my_list.append(tmp_list)

for i in my_list:
    print(i)