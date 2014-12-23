#!/usr/bin/python3.4

import signal

a = "abcdefghijklm"
b = "nopqrstuvxwyz"

c = list (input("Digite aqui o seu texto limpo: "))

for x in range(0, len(c)):
	for y in range(0, 12):
		if c[x] == a[y]:
			c[x] = b[y]
		else:
			if c[x] == b[y]:
				c[x] = a[y]

c = "".join(c)
print("Seu texto cifrado eh: " + c)
