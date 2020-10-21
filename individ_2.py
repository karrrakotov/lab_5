#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input("Введите слово: ")

    def palindrome_check(word):
        return word == word[::-1]
    if palindrome_check(word):
        print("Это слово палиндром")
    else:
        print("Это слово не палиндром")

