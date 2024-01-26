
#Ejercicio1: Define una función que tome dos números y retorne su suma

def suma(a, b):
  return a + b

suma(100, 0.5)

# Ejercicio2: Define una función que tome un número y retorne su factorial

def factorial(n):
  if n < 0:
    print ('El factorial de un negativo no está definido')
  factorial = 1
  for i in range (1, n+1):
    factorial *= i
  print(factorial)

factorial(10)

# Ejercicio3: Define una función que tome un número y determine si es primo

def primo(x):
  if x == 2:
    print(f'El número', x, 'es primo')
  elif x % 2 != 0:
    for i in range(3, int(x ** 0.5) + 1, 2):
      if x % 1 == 0:
        print(f'El número', x, 'no es primo')
        break
      else:
        print(f'El número', x, 'es primo')
  else:
    print(f'El número', x, 'es primo')

primo(80)

# Ejercicio4: Define una función que reciba una lista de números y retorne la suma de ellos

def sumatorio(list):
  suma = 0
  for i in list:
    suma = suma + i
  print(f'La suma total es:', suma)

sumatorio([1,2,3])

# Ejercicio5: Define una función que reciba una cadena de texto y retorne la cadena inversa

def invertir_cadena(cadena):
  cadena_invertida = ''
  for i in range(len(cadena) -1, -1, -1):
    cadena_invertida += cadena[i]
  return cadena_invertida
