#!/usr/bin/env python3
import re
import fileinput

def is_cyrillic(c):
  return bool(re.match('[а-яА-ЯёЁ]', c))

russ = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
russ_len = len(russ)
key = 'КРИПТОГРАФИЯ'
key_index = 0
key_len = len(key)

for l in fileinput.input():
  for c in l:
    if is_cyrillic(c):
      #print(c.upper(), russ.index(c.upper()), sep=', ', end=',\t')
      #print(key_index, key[key_index], russ.index(key[key_index]), sep=', ', end=',\t')
      cipher = (russ.index(c.upper()) + russ.index(key[key_index])) % russ_len
      key_index = (key_index + 1) % key_len
      #print(cipher, russ[cipher], sep=', ')
      print(russ[cipher], end='')


