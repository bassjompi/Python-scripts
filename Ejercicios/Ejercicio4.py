#!/usr/bin/python

num1 = input ('introduzca el primer numero: ')
num2 = input ('introduzca el segundo numero: ')
num3 = input ('introduzca el tercer numero: ')

if num1 > num2  and  num1>num3:
	print ('El mayor es {}'.format(num1))

elif num2 > num1 and num2 > num3:
	print ('El mayor es {}'.format(num2))

elif num3 > num1 and num3 > num2:
	print ('El mayor es {0}'.format(num3))

else:
	print ('Los tres numeros son iguales, morcipapas')
