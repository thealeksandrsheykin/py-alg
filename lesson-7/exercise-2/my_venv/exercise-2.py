# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50]. Выведите на экран исходный и отсортированный массивы.
'''
from random import randrange


if __name__ == '__main__':
    my_list = [None] * 10
    for i in range(len(my_list)):
        my_list[i] = randrange(0,50)
