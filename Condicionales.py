## Condicionales

# Ejercicio1: Dado un número, imprime si es positivo o negativo

numeros = ([1, -3, 5, 9])
for num in numeros:
  if num > 0:
    print(f'El número', num, 'es positivo')
  else: 
    print(f'El número', num, 'es negativo')


# Ejercicio2: Dado un número, imprime si es par o impar

numeros_2 = ([2,3,4,5,6,7,8,9,10])

for num in numeros_2:
  if num%2 == 0:
    print(f'El número', num, 'es par')
  else:
    print(f'El número', num, 'es impar')


# Ejercicio3: Dado tres números, encuentra y muestra el mayor de ellos

numeros_3 = ([15, 30, 40])

mayor = 0
for num in numeros_3:
  if num > mayor:
    mayor = num

print(f'El número', mayor, 'es el mayor de la lista')