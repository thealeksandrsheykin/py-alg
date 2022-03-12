# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
4.Определить, какое число в массиве встречается чаще всего.
'''
from random import randint

my_list = [randint(1,100) for i in range(10)]


my_tuple =(1, my_list[0])
for i in set(my_list):
    cnt = my_list.count(i)
    if cnt > my_tuple[0]:
        my_tuple = (cnt, i)
print(f'Число {my_tuple[1]} встречается в списке {my_list}: {my_tuple[0]}')


