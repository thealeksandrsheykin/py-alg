# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2.Закодировать любую строку по алгоритму Хаффмана
'''

import heapq
from collections import Counter,namedtuple


class Node:
    def __init__(namedtuple('Node',['left','right'])):
        self.right = right
        self.left = left
        self.value = value
