#!/usr/bin/python


cont = 0
M2 = []
M3 = []

while cont <= 100:
    cont = cont + 1
    if cont % 2 == 0:
        M2.append(cont)

    if cont % 3 == 0:
        M3.append(cont)

print ('la lista de multiplos de dos es: {0} '.format(M2))


print ('la lista de multiplos de tres es: {0} '.format(M3))