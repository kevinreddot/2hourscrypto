#!/usr/bin/python
# # -*- coding: utf-8 -*-
import sys

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".decode('utf-8')
plaintext = "маша".decode('utf-8')
key = "вася".decode('utf-8')
ans = ""

for i in range(len(plaintext)):
	char = plaintext[i]
	keychar = key[i % len(key)]
	alphIndex = (alphabet.index(keychar) + alphabet.index(char) ) % len(alphabet)
	enc = alphabet[alphIndex]
	ans += enc
	print char, keychar, enc
print(ans)
