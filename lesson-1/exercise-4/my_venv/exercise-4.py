# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
4.Написать программу, которая генерирует в указанных пользователем границах:
    -случайное целое число,
    -случайное вещественное число,
    -случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от
'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''

from random import randint,uniform

start = input('Старт: ')
end = input('Конец: ')

if start.isdigit() and end.isdigit():
    result = randint(0, (int(end) - int(start))) + int(start)
    print(f'Случайное целое число в диапозоне от {start} до {end}: {result}')
elif '.' in start or '.' in end:
    result = uniform(0, (float(end) - float(start))) + float(start)
    print(f'Вещественное число в диапозоне от {start} до {end}: {result}')
else:
    result = randint(0,(int(ord(end)) - int(ord(start)))) + int(ord(start))
    print(f'Случайный символ в диапозоне от "{start}" до "{end}": {chr(result)}')





