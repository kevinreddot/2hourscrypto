#!/usr/bin/python
# # -*- coding: utf-8 -*-
import sys

russ = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя".decode('utf-8')
word = "маша".decode('utf-8')
key = "вася".decode('utf-8')
ans = ""



for char, keychar in zip(word,key):
  charalphabet = russ[russ.index(keychar):]
  shift = russ.index(keychar)
  enc = charalphabet[charalphabet.index(char)+shift]
  ans += enc
  print char, keychar, enc
print(ans)
