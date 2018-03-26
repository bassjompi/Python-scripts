#!/usr/bin/python

def function():
    long = input('cuantos elementos quiere en la lista? ')
    dupfree=set()
    lista = []
    for i in range(long):
        num = input('Introduzca un numero: ')
        lista.append(num)

    for i in lista:
        dupfree.add(i)

    print(lista)
    print(dupfree)

function()






