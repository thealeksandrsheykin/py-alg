# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
'''

n = int(input('Введите число: '))

# 1. Способ
f = 0
for i in range(1,n+1):
    f += i
s = n*(n+1)/2

print(f'Первая: {f}\n'
      f'Вторая: {s}')

# 2. Способ
def first(n):
    if n == 1:
        return n
    elif n > 0:
        return n + first(n-1)

def second(n):
    return n * (n + 1) // 2

n = int(input('Введите число: '))
print(f'Первая: {first(n)}')
print(f'Вторая: {second(n)}')



