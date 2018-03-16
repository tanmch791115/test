__author__ = 'tanmch791115'


# coding=utf-8
# _*_ coding: utf-8 _*_
from itertools import cycle


def crypt1(source, key):

    def func(x, y): return chr(ord(x) ^ ord(y))
    return ''.join(map(func, (source), (list(key))))


def crypt(source, key):
    cycleKey = cycle(key)
    result = ''
    for i in source:

        result = result+(chr(ord(i) ^ ord(cycleKey.next())))
    return result


source = 'Beautiful is better than ugly!'
key = 'Python'
print('Before encrypted: ' + source)
encrypted = crypt(source, key)
print('After encrypted: ')
print(encrypted)
decrypted = crypt(encrypted, key)
print('After decrypted: ' + decrypted)
