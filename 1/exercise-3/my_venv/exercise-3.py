# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
3.По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
'''

p1 = input('Введите координаты первой точки (X1,Y1): ')
p2 = input('ВВедите коордианты второй точки (X2,Y2): ')

x1,y1 = p1.split(',')
x2,y2 = p2.split(',')

k = (int(y1) - int(y2))/(int(x1) - int(x2))
b = int(y2) - k * int(x2)

if str(b).startswith('-'):
    print(f'y = {k}x - {str(b)[1:]}')
else:
    print(f'y = {k}x + {b}')



