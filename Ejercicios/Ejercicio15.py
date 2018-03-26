#!/usr/bin/python
import sys

n = 3

while n != 0:
    clave = raw_input("Inserte la clave por favor: ")
    if clave  == 'eureka':
        print('felicidades hijo de puta')
        sys.exit(0)

    else:
        n = n - 1

print('no sabes la clave')
