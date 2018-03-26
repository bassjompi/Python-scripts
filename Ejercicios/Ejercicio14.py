#!/usr/bin/python

limite = input('inserte el numero para la suma: ')
cont = 0
cont2 = 0
suma= 0

while cont < limite:    #cuenta los numeros pares
    cont2 = cont2 +1     #cuenta todos los numeros
    if cont2 % 2 == 0:
        suma = suma + cont2
        cont = cont +1

print ('la suma es {0}'.format(suma))

