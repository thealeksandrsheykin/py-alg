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
    if my_func(i) > my_tuple[1]:
        my_tuple = (i,my_func(i))
    else: continue

print(f'Сумма цифры: {my_tuple[0]}: {my_tuple[1]}')