#A N A L I S I S
'''
Vocales = 4
'''


palabra = 'analisis'
contadorPalabras = 0



if palabra[0] == 'a' or palabra[0] == 'e' or palabra[0] == 'i' or palabra[0] == 'o' or palabra[0] == 'u':
    contadorPalabras = contadorPalabras + 1
if palabra[1] == 'a' or palabra[1] == 'e' or palabra[1] == 'i' or palabra[1] == 'o' or palabra[1] == 'u':
    contadorPalabras = contadorPalabras + 1
if palabra[2] == 'a' or palabra[2] == 'e' or palabra[2] == 'i' or palabra[2] == 'o' or palabra[2] == 'u':
    contadorPalabras = contadorPalabras + 1
if palabra[3] == 'a' or palabra[3] == 'e' or palabra[3] == 'i' or palabra[3] == 'o' or palabra[3] == 'u':
    contadorPalabras = contadorPalabras + 1
if palabra[4] == 'a' or palabra[4] == 'e' or palabra[4] == 'i' or palabra[4] == 'o' or palabra[4] == 'u':
    contadorPalabras = contadorPalabras + 1
if palabra[5] == 'a' or palabra[5] == 'e' or palabra[5] == 'i' or palabra[5] == 'o' or palabra[5] == 'u':
    contadorPalabras = contadorPalabras + 1
if palabra[6] == 'a' or palabra[6] == 'e' or palabra[6] == 'i' or palabra[6] == 'o' or palabra[6] == 'u':
    contadorPalabras = contadorPalabras + 1
if palabra[7] == 'a' or palabra[7] == 'e' or palabra[7] == 'i' or palabra[7] == 'o' or palabra[7] == 'u':
    contadorPalabras = contadorPalabras + 1


print('La cantidad de vocales es: ', str(contadorPalabras))


vocales = ['a','e','i','o','u']

contadorPalabras = 0

for l in palabra:
    if l in vocales:
        contadorPalabras +=1

print ('La cantidad de palaras es ', str(contadorPalabras))
