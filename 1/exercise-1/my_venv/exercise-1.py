# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

number = int(input('Введите трехзначное число: '))

a = number//100
b = (number//10) % 10
c = number % 10

print(f'Произведение цифр трехзначного числа({number}): {a*b*c}')
print(f'Сумма цифр трехзначного числа({number}): {a+b+c}')

