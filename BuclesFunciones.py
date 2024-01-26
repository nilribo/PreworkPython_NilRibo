# Ejercicio1: crea una función para verificar si un número es par o impar y devuelva
# 'El número es par' o 'El número es impar' según corresponda

numero = input("Introduce: ")

def es_par():
    numero = None
    try:
        numero = int(numero)
    except ValueError:
        return 'El numero no es válido'

    if numero % 2 == 0:
        return 'El número es par'
    else:
        return 'El número es impar'


# Ejercicio2: Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado

def factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    numero = int(input("Introduce un número: "))
    print(f"El factorial de {numero} es {factorial(numero)}")


# Ejercicio3: Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de "La cantidad de dígitos es: " y el resultado total de dígitos

def digitos(numero):
    return len(str(numero))

numero = int(input("Ingresa un número: "))
print(f'La cantidad de dígitos es: ', digitos(numero))


# Ejercicio4: Dada una lista de números, crea una función que devuelva el número máximo de la lista

def num_maximo(lista):
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

numeros = [0, 5, 10, 15, 30]
print(f'El número máximo de la lista es el: ', num_maximo(numeros))


# Ejercicio5: Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado

def suma_digitos(numero):
    numero_str = str(numero)        # numero 123 = "123"
    suma = 0
    for digito in numero_str:       # "123"[0] = 1; "123"[1] = 2; "123"[2] = 3
        suma += int(digito)         # suma += 1; += 1+2; += 1+2+3
    return suma                     # suma = 1 + 2 + 3

numero = int(input('Inserta un número: '))
print(f'La suma de los dígitos es: ', suma_digitos(numero))


# Ejercicio6: Dados dos números, crea una función para encontrar el mínimo común múltiplo de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM

def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        maximo = max(a, b)
        while True:
            if maximo % a == 0 and maximo % b == 0:
                return maximo
            maximo += 1

num1 = int(input("Entra el primer numero: "))
num2 = int(input("Entra el segundo numero: "))
print('El MCM es: ', mcm(num1, num2))

# Ejercicio7: Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo

def area(a,b):
  sum_area = (a * b)/2
  return sum_area

num1 = float(input('Incorpora el valor de la base: '))
num2 = float(input('Incorpora el valor de la altura: '))
print(f'La area del triángulo es: ', area (num1, num2))


# Ejercicio8: Crea una función que, dado un número, verifique si un número es positivo, negativo o cero

def natural(num):
  if num == 0:
    print(f'El número es zero')
  else:
    if num > 0:
      print(f'El número es positivo')
    else:
      print(f'El número es negativo')

num = int(input('Ingresa un número: '))
print(natural(num))

# Ejercicio9: Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra

def cantidad(palabra):
    contador = 0
    for letra in palabra:
        if palabra.isalpha():
            contador += 1
    return contador

palabra = input("Inserta la palabra: ")
print(f'La palabra tiene', cantidad(palabra), 'letras')

# Ejercicio10: Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto

def lista(absolutos):
    for i in range (len(absolutos)):
        absolutos[i] = abs(absolutos[i])
    return absolutos

absolutos = [5, -12, 0]
print(f'Lista con valores absolutos: ', lista(absolutos))

# Ejercicio11: Crea una función que, dado un número, verifique si un número es primo

def numero(primo):
    if primo <= 1:
        return False
    for i in range (2, primo):
        if primo % i == 0:
            return False
        return True

primo = int(input('Inserta un número: '))
if numero(primo):
    print('Es un número primo')
else:
    print('No es un número primo')


# Ejercicio12: Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números

def mcd(a,b):
    while b:
        a, b = b, a % b
    return a

a = int(input('Ingresa el primer número: '))
b = int(input('Ingresa el segundo número: '))
print(f'El MCD es: ', mcd(a,b))