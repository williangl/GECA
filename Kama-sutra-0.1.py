#!/usr/bin/python3.4

import signal

a = "abcdefghijklm"
b = "nopqrstuvxwyz"

c = list (input("Digite aqui o seu texto limpo: ")) 
#converte a string em lista para melhor funcionalidade no IF

alfaA = "àáãäâ"
alfaE = "èéẽëê"
alfaI = "ìíĩïî"
alfaO = "òóõöô"
alfaU = "ùúũüû"

for x in range(0, len(c)):
	#debug para alguns caracteres especiais
	if c[x] == 'ç':
			c[x] = 'c'
	for z in range(0, len(alfaA)):
		if c[x] == alfaA[z]:
			c[x] = 'a'
		elif c[x] == alfaE[z]:
			c[x] = 'e'
		elif c[x] == alfaI[z]:
			c[x] = 'i'
		elif c[x] == alfaO[z]:
			c[x] = 'o'
		elif c[x] == alfaU[z]:
			c[x] = 'u'
	#fim do debug
	
	for y in range(0, 12):
		if c[x] == a[y]:
			c[x] = b[y]
		else:
			if c[x] == b[y]:
				c[x] = a[y]

c = "".join(c) #converte a lista em string novamente
print("Seu texto cifrado eh: " + c)
