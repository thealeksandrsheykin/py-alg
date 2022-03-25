# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименова-
ния предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''

# Cпособ №1
n = int(input('Введите данные о количестве предприятий: '))
my_list = [None] * n
total = 0

for i in range(n):
    name = input(f'Введите наименование предприятия №{i+1}: ')
    profit = 0
    for j in range(4):
        profit += float(input(f'Введите прибыль за {j+1} квартал: '))
    my_list[i] = (name,profit)
    total += profit
avg = total/n
print(f'\nСредняя прибыль за год для всех предприятий: {avg:.2f}')
print(f'Предприятия, у которых прибыль выше среднего:')
for i in my_list:
    if i[1] >= avg:
        print(f'\tПредприятие: {i[0]}\tПрибыль: {i[1]:.2f}')
print(f'Предприятия, у которых прибыль ниже среднего:')
for i in my_list:
    if i[1] <= avg:
        print(f'\tПредприятие: {i[0]}\tПрибыль: {i[1]:.2f}')


# Способ №2
from collections import namedtuple
from random import randrange

company = namedtuple('company',['name','total_profit'])
n = int(input('Введите данные о количестве предприятий: '))
my_list = [None] * n
total = 0

for i in range(n):
    name = input(f'Введите наименование предприятия №{i + 1}: ')
    profit = 0
    for j in range(4):
        tmp_var = float(randrange(0,10000000)) # input(f'Введите прибыль за {j+1} квартал: ')
        print(f'Введите прибыль за {j+1} квартал:  {tmp_var}')
        profit += tmp_var
    my_list[i] = company(name=name,total_profit=profit)
    total += profit

avg = total/n
print(f'\nСредняя прибыль за год для всех предприятий: {avg:.2f}')
print(f'Предприятия, у которых прибыль выше среднего:')
for i in my_list:
    if i.total_profit >= avg:
        print(f'\tПредприятие: {i.name}\tПрибыль: {i.total_profit:.2f}')
print(f'Предприятия, у которых прибыль ниже среднего:')
for i in my_list:
    if i.total_profit <= avg:
        print(f'\tПредприятие: {i.name}\tПрибыль: {i.total_profit:.2f}')








