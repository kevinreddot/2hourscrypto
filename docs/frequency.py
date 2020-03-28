#!/usr/bin/env python3
import re
import fileinput

def is_cyrillic(c):
  return bool(re.match('[а-яА-ЯёЁ]', c))

freq = {}
for line in fileinput.input():
  for char in line:
    if is_cyrillic(char):
      uchar= char.upper()
      if uchar in freq:
        freq[uchar] += 1
      else:
        freq[uchar] = 1
for i in sorted(freq):
  print (i, freq[i], sep=", ")
