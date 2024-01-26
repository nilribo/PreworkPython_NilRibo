# Ejercicio1: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci

def fibonacci(n):
  a = 0
  b = 1
  for i in range(n):
    print(a)
    a, b = b, a + b
fibonacci(10)

# Ejercicio2: Define una función que tome un número y retorne una lista de sus divisores

def divisores(numero):
    return [i for i in range(1, numero + 1) if numero % i == 0]

print(divisores(10))

# Ejercicio3: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original

def original(lista):
  return {elemento for elemento in lista}

print(original([1,1,2,3,4,5,5]))

# Ejercicio4: Define una función que tome un número y retorne la suma de sus dígitos

def suma_digitos(numero):
  numero_str = str(numero)
  suma = 0
  for digito in numero_str:
    suma += int(digito)
  return suma

numero = int(input('Inserta un número: '))
print(f'La suma de los dígitos es: ', suma_digitos(numero))

# Ejercicio5: Define una función que tome una cadena y cuente el número de vocales en la cadena

def vocales(lista):
  vocales = 0
  for vocal in lista:
    if vocal in "aeiouáéíóú":
      vocales += 1
  return vocales

print(vocales('Hola Mundo!'))

# Ejercicio6: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista

def elementos(lista, n):
  return lista[:n]

print(elementos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 5))

# Ejercicio7: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena

def contar_letras(cadena):
  mayusculas = 0
  minusculas = 0
  for caracter in cadena:
    if caracter.isupper():
      mayusculas += 1
    elif caracter.islower():
      minusculas += 1
  return mayusculas, minusculas

print(contar_letras("Hello World"))

# Ejercicio8: Define una función que tome un número y retorne TRUE si es un número perfecto, false en caso contrario. 

def es_perfecto(numero):
  suma = 1
  for i in range (2, numero):
    if numero % i == 0:
      suma += i
  return suma == numero

print(es_perfecto(20))

# Ejercicio9: Define una función que reciba un número y retorne su representación en binario

def a_binario(numero):
  return bin(numero).replace("0b", "")

print(a_binario(10))

# Ejercicio10: Define una función que reciba dos listas y retorne la intersección de ambas

def interseccion(lista1, lista2):
  interseccion = []
  for elemento in lista1:
    if elemento in lista2:
      interseccion.append(elemento)
  return interseccion

print(interseccion([1,2,3,4], [2,3,4,5]))


# Ejercicio11: Define una función que tome una cadena y determine si es un palíndromo

def palindromo(cadena):
  cadena_invertida = cadena[::-1]
  return cadena == cadena_invertida

print(palindromo("radar"))

# Ejercicio12: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima "Fizz" en lugar del número y para los múltiplos de cinco imprima "Buzz". Para números que son multiples de tanto tres como cinco, imprima "FizzBuzz"

for i in range (1, 51):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)


# Ejercicio13: Define una función que tome una lista y retorne la lista ordenada en orden ascendente

def ascendente(lista):
  return sorted(lista)

print(ascendente([1,2,3,4,5,6,7,8,9,10]))

# Ejercicio14: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n

def mas_largo(lista, n):
  return [palabra for palabra in lista if len(palabra) > n]

print(mas_largo(["hola", "nerd", "balon", "pelota", "porteria"], 4))


# Ejercicio15: Define una función que tome un número y calcule su serie de Fibonacci

def fib(n):
  serie = []
  a, b = 0, 1
  for i in range (n):
    serie.append(a)
    a, b = b, a + b
  return serie

print(fib(10))

# Ejercicio16: Define una función que tome una lista de números y retorne el número más grande de la lista

def mayor(lista):
  return max(lista)

lista = [0, 10, 22, 15, 105]
mayor = mayor(lista)
print(mayor)

# Ejercicio17: Define una función que reciba un número y retorne la suma de sus dígitos al cubo

def cubo(numero):
  numero_str = str(numero)
  suma = 0
  for i in numero_str:
    suma += int(i)**3
  return suma

print(cubo(123))

# Ejercicio18: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista

def segundo(lista):
  lista.sort(reverse = True)
  return lista[1]

print(segundo([10, 20, 15, 30]))

# Ejercicio19: Define una función que tome dos listas y retorne TRUE si tienen al menos un miembro en común, de lo contrario, retorne FALSE

def comun(lista1, lista2):
  for i in lista1:
    if i in lista2:
      return True
  return False

lista1 = [1,2,3,4]
lista2 = [0]
print(comun(lista1, lista2))

# Ejercicio20: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso

def reverse(lista):
  lista_invertida = lista[::-1]
  return lista_invertida

print(reverse("Hello World"))

# Ejercicio21: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene

def numero(cadena):
  digitos = len([caracter for caracter in cadena if caracter.isdigit()])
  letras = len([caracter for caracter in cadena if caracter.isalpha()])
  return {'digitos': digitos, 'letras': letras}

print(numero("a123b4b31ajj"))

# Ejercicio22: Define una función que reciba una lista de números y retorne la suma acumulada de los números

def suma(numeros):
  return [sum(numeros[:i]) for i in range (len(numeros) + 1)]

numeros = [1, 2, 3, 4]
suma = suma(numeros)
print(suma)

# Ejercicio23: Define una función que encuentre el elemento más común en una lista

def comun(lista):
  frecuencia = {}
  for elemento in lista:
    if elemento in frecuencia:
      frecuencia[elemento] += 1
    else:
      frecuencia[elemento] = 1
  comun = max(frecuencia, key = frecuencia.get)
  return comun

print(comun([1,1,2,2,2,3,3,3,5,5]))

# Ejercicio24: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10

def tabla(n):
  return {i: n * i for i in range(1, 11)}
print(tabla(3))

# Ejercicio25: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena

def cantidad(cadena):
  return {caracter: cadena.count(caracter) for caracter in cadena}

print(cantidad("Hello World"))

# Ejercicio26: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas

def no_esta(lista1, lista2):
  conjunto1 = set(lista1)
  conjunto2 = set(lista2)
  diferencia = conjunto1 ^ conjunto2
  no_esta = list(diferencia)
  return no_esta

print(no_esta([0,1,2,3],[2,3,4,5]))

# Ejercicio27: Define una función que tome una lista y retorne la lista sin duplicados

def sinduplicados(lista):
  no_duplicados = []
  for i in lista:
    if i not in no_duplicados:
      no_duplicados.append(i)
  return no_duplicados

print(sinduplicados([1,1,2,3,3,4,1,2,3,4,5]))

# Ejercicio28: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número

def cuadrados(n):
  return sum([i**2 for i in range (2, n + 1, 2)])

print(cuadrados(4))

# Ejercicio29: Define una función que reciba una lista de numeros y retorne el promedio de los números en la lista

def promedio(lista):
  suma = 0
  for numero in lista:
    suma += numero
  return float(suma/len(lista))

print(promedio([15, 30, 45]))

import statistics
def promedio(lista):
  return statistics.mean(lista)

print(promedio([15, 30, 45]))

# Ejercicio30: Define una función que reciba una lista de cadenas y retorne la cadena más larga de la lista

def cadena_larga(lista):
  return max(lista, key = len)

lista = ["hola", "mundo", "Python"]
cadena_larga = cadena_larga(lista)
print(cadena_larga)

# Ejercicio31: Define una función que reciba un numero entero n y retorne una lista con los primeros n numeros primos

def primeros_n_primos(n):
  primos = [2]
  for i in range(3, n + 1):
    divisible = False
    for j in primos:
      if i % j == 0:
        divisible = True
        break
    if not divisible:
      primos.append(i)
  return primos

print(primeros_n_primos(10))

# Ejercicio32: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso

def inverso(cadena):
  return cadena[::-1]

print(inverso("Hello, World!"))

# Ejercicio33: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla

def ordenar_por_ultimo_elemento(lista_de_tuplas):
    lista_ordenada = sorted(lista_de_tuplas, key=lambda x: x[-1])
    return lista_ordenada

tuplas_a_ordenar = [(1, 3, 5), (4, 2, 8), (7, 1, 3)]
resultado = ordenar_por_ultimo_elemento(tuplas_a_ordenar)
print(resultado)

# Ejercicio34: Define una funcion que reciba una cadena y retorne la cantidad de letras vocales de la cadena

def cadena(vocales):
  contador = 0
  for vocal in vocales:
    if vocal in 'aeiouáéíóú':
      contador += 1
  return contador

print(cadena("Hello World"))

# Ejercicio35: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario False

def primo(n):
  n = int(n)
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
    else:
      return True

print(primo(8))