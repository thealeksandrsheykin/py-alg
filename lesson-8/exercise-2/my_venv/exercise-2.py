# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2.Закодировать любую строку по алгоритму Хаффмана
'''

from heapq import heapify, heappop, heappush
from collections import namedtuple, Counter


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(data):
    queue = list()
    for char, freq in Counter(s).items():
        queue.append((freq, len(queue), Leaf(char)))
    heapify(queue)




if __name__ == '__main__':
    s = input('Введите строку: ')
    code = huffman_encode(s)
