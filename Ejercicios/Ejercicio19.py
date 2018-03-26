#!/usr/bin/python
import sys

meses = ['dummy','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

dia = input('Introduzca el dia: ')
if (dia > 31)  or (dia < 1):
    print ('El dia es incorrecto')
    sys.exit(1)


mes = input('Introduzca el mes: ')
if mes > 12  or mes < 1:
    print ('El mes es incorrecto')
    sys.exit(1)

anyo = input('Introduzca el anyo: ')
if anyo <= 0:
    print ('El anyo es incorrecto')
    sys.exit(1)


print('{0} de {1} de {2}'.format(dia,meses[mes],anyo))

