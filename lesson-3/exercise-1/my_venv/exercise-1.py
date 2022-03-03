# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
1.В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

my_dict = dict.fromkeys(['2','3','4','5','6','7','8','9'], 0)
for i in range(2,100):
    for j in range(2,10):
        if i % j == 0:
            my_dict[str(j)] += 1
        else: continue

for i,j in my_dict.items():
    print(f'Число {i}: {j}')