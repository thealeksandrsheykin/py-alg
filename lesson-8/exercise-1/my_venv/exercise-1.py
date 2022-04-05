# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
1.Определить количество различных подстрок с использованием хеш-функции. Задача: на вход функции дана строка, требуется
вернуть количество различных подстрок в этой строке.

Примечание: в сумму не включаем пустую строку и строку целиком.
'''

import hashlib
from random import choice
from string import ascii_lowercase


def number_substring(s):
    my_set = set()
    length = len(s)
    for i in range(length):
        for j in range(i+1,length+1):
            if length == len(s[i:j]):
                break
            else:
                my_set.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    return len(my_set)


if __name__ == '__main__':
    n = int(input('Введите длину строки: '))
    s = ''.join(choice(ascii_lowercase) for _ in range(n))
    print(f'Строка: {s}')
    print(f'Количество подстрок в строке: {number_substring(s)}')
