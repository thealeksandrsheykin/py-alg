# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2.Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо
и влево на два знака.
'''

a = 5
b = 6

# Логическое "И"
res_and = a & b
print(f'{bin(a)[2:]} & {bin(b)[2:]} = {bin(res_and)[2:]}')

# Логическое "ИЛИ"
res_or = a | b
print(f'{bin(a)[2:]} | {bin(b)[2:]} = {bin(res_or)[2:]}')

# Логическое исключающее "ИЛИ"
res_xor = a ^ b
print(f'{bin(a)[2:]} ^ {bin(b)[2:]} = {bin(res_xor)[2:]}')

# Побитовый сдвиг вправо на два знака числа 5
res_shift_right = a >> 2
print(f'{bin(a)[2:]} >> {bin(res_shift_right)[2:]}')

# Побитовый сдвиг влево на два знака числа 5
res_shift_left = a << 2
print(f'{bin(a)[2:]} << {bin(res_shift_left)[2:]}')


