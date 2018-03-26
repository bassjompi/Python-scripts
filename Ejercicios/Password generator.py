#!/usr/bin/python
import random
import string


caracteres = ['','!','@','#','%','^','&','*','=']
numeros = [1,2,3,4,5,6,7,8,9]
mayusculas = list(string.ascii_uppercase)
strenght = input('Please choose the type of password:\n1- Weak\n2- Medium\n3- Strong\n')



if strenght == 1: #crea una contrasenya debil a base de dos palabras

    palabras = raw_input('Escriba una frase larga \n\n')
    repo=palabras.split()
    repo2= random.sample(repo,2)

    password=''.join(repo2)  #UNIRLO AL FINAL
    print(password)

elif strenght == 2:  #crea una contrasenya media a base de palabras con numeros o caracteres especiales

    palabras = raw_input('Escriba una frase larga \n\n')
    repo = palabras.split()
    repo2 = random.sample(repo, 2)  #lista con dos palabras
    repo3 = random.sample(caracteres,1)
    repo2.extend(repo3) #anadido un caracter especial

    password = ''.join(repo2)  #UNIRLO AL FINAL
    print(password)


elif strenght == 3: #crea una contrasenya fuerte, con al menos 8 caracteres, numero/s, caracteres especiales y Mayuscula

    palabras = raw_input('Escriba una frase larga \n\n')
    repo = palabras.split()
    repo2 = random.sample(repo, 3)  # lista con tres palabras
    repo3 = random.sample(caracteres, 3)
    repo4 = random.sample(numeros,3)
    repo5 = random.sample(mayusculas,2)

    repo2.extend(repo3)  # anadidos tres caracteres especiales
    repo2.extend(repo4)  # anadidos tres numeros
    repo2.extend(repo5)  # anadidos dos mayusculas

    password = ''.join(repo2)  #UNIRLO AL FINAL
    print(password)