# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Определить, является ли год, который ввел пользователем, високосным или не високосным.
'''

year = int(input('Введите год: '))

if year % 4 == 0:
    print(f'Год является високосным...')
elif year % 100 == 0:
    if year % 400 == 0:
        print(f'Год является високосным...')
    else:
        print(f'Год не является високосным...')
else:
    print(f'Год не является високосным...')

