#!/usr/bin/python
import sys

cont=0
lado = input (" Introduzca el tamanyo: ")


for i in range(lado):
    print('\n')
    cont = 0
    while cont != lado:
        cont = cont +1
        if i == 0 or i == (lado -1):
            sys.stdout.write('*')


        else:
            if cont == 1 or cont == lado:
                sys.stdout.write ('*')

            else:
                sys.stdout.write(' ')


