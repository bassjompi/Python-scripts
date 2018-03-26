#!/usr/bin/python

ninos = input ('introduzca el numero de chicos ')
ninas = input(' Introduzca el numero de chicas ')
total= ninos + ninas

pninos= ninos * 100 / total
pninas= ninas * 100 / total

print('El porcentaje de ninos es del {0}% y el de ninas es del {1}%'.format(pninos,pninas))