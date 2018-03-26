#!/usr/bin/python

frase = raw_input('introduzca su frase: ')
cortar = frase.split(" ")

cortar.reverse()

str(cortar)

final =' '.join(cortar)

print (final)


