# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

'''
def convert_to_list(data):
    return [i for i in data]

a = input('Введите первое число в формате HEX: ')
b = input('Введите второе число в формате HEX: ')

my_list_a = convert_to_list(a.upper())
my_list_b = convert_to_list(b.upper())

# Способ №1
c_sum = hex(int(''.join(a), 16) + int(''.join(b), 16))
my_list_sum = convert_to_list(c_sum[2:].upper())
print(f'Сумма чисел {a.upper()} и {b.upper()} = {c_sum[2:].upper()} или {my_list_sum}')

c_mul = hex(int(''.join(a), 16) * int(''.join(b), 16))
my_list_mul = convert_to_list(c_mul[2:].upper())
print(f'Произведение чисел {a.upper()} и {b.upper()} = {c_mul[2:].upper()} или {my_list_mul}')
'''

# Cпособ №2
import collections

HEX_DICT = {'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
            '8':8,'9':9, 'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

def edit_data(x,y):
    deq_x = collections.deque(x)
    deq_y = collections.deque(y)
    if len(deq_y) > len(deq_x):
        deq_x, deq_y = deq_y, deq_x
    deq_y.extendleft('0' * (len(deq_x) - len(deq_y)))
    return (deq_x, deq_y)

def sum_data(x,y):
    x,y = edit_data(x,y)
    result = collections.deque()
    flag = 0
    for i in range(len(x) - 1, -1, -1):
        my_var = HEX_DICT[x[i]] + HEX_DICT[y[i]] + flag
        if my_var >= 16:
            my_var -= 16
            flag = 1
        else:
            flag = 0
        result.appendleft(list(HEX_DICT.keys())[my_var])
    if flag:
        result.appendleft('1')
    return list(result)

def mul_data(x,y):
    x,y = edit_data(x,y)
    result = collections.deque('0')
    for i in range(len(x) - 1, -1, -1):
        my_var = HEX_DICT[y[i]]
        tmp_list = collections.deque('0')
        for _ in range(my_var):
            tmp_list = sum_data(tmp_list,x)
        tmp_list.extend('0' * (len(x) - i - 1))
        result = sum_data(result,tmp_list)
    return list(result)


x = (input('Введите первое число в формате HEX: ')).upper()
y = (input('Введите второе число в формате HEX: ')).upper()

print(f'Сумма чисел {x} + {y} = {sum_data(x,y)}')
print(f'Произведение чисел {x} * {y} = {mul_data(x,y)}')