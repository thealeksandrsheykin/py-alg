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
class My_class():
    def __init__(self,data):
        self.bin    = {'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
                     '8':8,'9':9, 'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        self.hex    = list(self.bin.keys())
        self.data   = data
        self.result = list()

    def __add__(self, other):
        print(True,self.data,other.data)
        if len(other.data) > len(self.data):
            self.data, other.data = other.data, self.data
        other.data = ['0' for _ in range(len(self.data) - len(other.data))] + other.data
        flag = 0
        for i in range(len(self.data)-1,-1,-1):
            data_result = self.bin[self.data[i]] + self.bin[other.data[i]] + flag
            if data_result >= 16:
                data_result -= 16
                flag = 1
            else:
                flag = 0
            self.result.append(self.hex[data_result])
        if flag:
            self.result.append('1')
        return self.result[::-1]

    def __mul__(self, other):
        if len(other.data) > len(self.data):
            self.data,other.data = other.data,self.data
        other.data = ['0' for _ in range(len(self.data)-len(other.data))] + other.data
        result = ['0']
        for  i in range (len(self.data)-1,-1,-1):
            data_2 = self.bin[other.data[i]]
            print(data_2)

            tmp_list = ['0']
            for _ in range(data_2):
                print(True)
                tmp_list = self.data.__add__(tmp_list)
                print(tmp_list)

            tmp_list.extend('0'*(len(self.data)-i-1))
          #  print(spam)
          #  result = tmp_list.__add__(result)
           # print(result)
        return result





a = list((input('Введите первое число в формате HEX: ')).upper())
b = list((input('Введите второе число в формате HEX: ')).upper())

x = My_class(a)
y = My_class(b)

print(f'Сумма чисел: {a} + {b} = {x+y}')
print(x*y)