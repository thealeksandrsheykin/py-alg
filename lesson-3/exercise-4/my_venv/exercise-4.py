# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
4.Определить, какое число в массиве встречается чаще всего.
'''

n = int(input('Введите кол-во чисел в массиве: '))
my_list = [int(input(f'Введите {i} элемент списка: ')) for i in range(n)]

# 1. Способ
my_dict = dict.fromkeys(list(set(my_list)),0)
my_dict = {i: my_list.count(i) for i in set(my_list)}


'''
result = list()
for i,j in my_dict.items():
    f = False
    for k,v in my_dict.items():
        if j == v and i != k:
            f = True
            break
        else: continue
    if f:
        result.append(i)

if not result:
    print(f'Число {max(my_dict, key=my_dict.get)} встречается в списке {my_list} чаще всего')
else:
    print(f'Числa {result} встречается в списке {my_list} одинаковое кол-во раз')
'''


# 2. Способ
a = 0
for i in range(len(my_list)):
    f = False
    for j in range(len(my_list)):
        if my_list[i] == my_list[j] and i != j:
            f = True
    if f:
        a = my_list[i]
print(f'Число {a} встречается в списке {my_list} чаще всего')

