#!/usr/bin/python
# # -*- coding: utf-8 -*-
import sys

class Vigener:
	def __init__(self, alphabet, key):
		self.alphabet = alphabet
		self.key = key

	def setKey(self, key):
		self.key = key

	def setAlphabet(self, alphabet):
		self.alphabet = alphabet

	def __encDec(self, text, isEncrypt):
		ans = ""
		for i in range(len(text)):
			char = text[i]
			keychar = self.key[i % len(self.key)]
			alphIndex = (self.alphabet.index(char) + isEncrypt * self.alphabet.index(keychar) ) % len(self.alphabet)
			enc = self.alphabet[alphIndex]
			ans += enc
			print char, keychar, enc
		return ans

	def encrypt(self, plaintext):
		return self.__encDec(plaintext, 1)

	def decrypt(self, ciphertext):
		return self.__encDec(ciphertext, -1)

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".decode('utf-8')
plaintext = "маша".decode('utf-8')
key = "вася".decode('utf-8')

v = Vigener(alphabet, key)
c = v.encrypt(plaintext)
print c
print v.decrypt(c)
