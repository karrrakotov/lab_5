#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    bad_chars = ['с', 'c']
    s = ''.join(i for i in s if not i in bad_chars)
    print("Предложение после замены: " + s)
