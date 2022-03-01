# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его
цифр.
'''
from random import randint

def my_func(n):
    if n < 10:
        return n
    else:
        return n % 10 + my_func(n // 10)



list_numbers = [randint(0,9999) for _ in range(4)]
my_tuple = (0,0)
for i in list_numbers:
    tmp_data = my_func(i)
    if tmp_data > my_tuple[1]:
        my_tuple = (i,tmp_data)
    else: continue

print(f'Сумма цифры: {my_tuple[0]}: {my_tuple[1]}')