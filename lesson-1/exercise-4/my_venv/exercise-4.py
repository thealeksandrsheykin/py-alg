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

# Случайное целое число
start = int(input('Старт: '))
end   = int(input('Конец: '))

result = randint(0,(end - start)) + start
print(f'Случайное целое число в диапозоне от {start} до {end}: {result}')

# Случайное вещественное число
start = float(input('Старт: '))
end   = float(input('Конец: '))

result = uniform(0,(end-start)) + start
print(f'Вещественное число в диапозоне от {start} до {end}: {result}')

# Случайный символ
start = input('Старт: ')
end   = input('Конец: ')

result = randint(0,(int(ord(end)) - int(ord(start)))) + int(ord(start))
print(f'Случайный символ в диапозоне от "{start}" до "{end}": {chr(result)}')





