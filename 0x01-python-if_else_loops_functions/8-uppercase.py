#!/usr/bin/python3
def uppercase(str):
	for i in str:
		if ord(i) >= 97 and ord(i) < 123:
			char = chr(ord(i) - 32)
		else:
			char = i
		print(char, end="")
	print('')
