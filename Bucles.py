# Ejercicio1: Imprime los números del 1 al 10 usando un bucle for

list = ([1,2,3,4,5,6,7,8,9,10])

for num in list:
  print(num)

# Ejercicio2: Imprime los números pares del 1 al 20 usando while

pares = []
cont = 1
while cont <= 20:
  if cont%2 == 0:
    pares.append(cont)
  cont += 1

print(pares)

# Ejercicio3: Usa un bucle para calcular la suma de los números del 1 al 100

lista = []
count = 0
while count <= 100:
  lista.append(count)
  count += 1

print(sum(lista))