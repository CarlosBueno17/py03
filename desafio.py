
numeros = []
while True:
     numero = int(input("Digite um número (ou 0 para encerrar): "))
     if numero == 0:
        break
     numeros.append(numero)

    # Separar números pares e ímpares
numeros_pares = [num for num in numeros if num % 2 == 0]
numeros_impares = [num for num in numeros if num % 2 != 0]

# Ordenar as listas
numeros_pares.sort()
numeros_impares.sort()

# Imprimir números ordenados
print("\nNúmeros pares em ordem crescente:", numeros_pares)
print("Números ímpares em ordem crescente:", numeros_impares)

# Calcular e imprimir a soma dos números
soma_total = sum(numeros)
print("\nSoma total dos números:", soma_total)

# quantidade de numeros inseridos
quantidade_de_numeros = len(numeros)
print(f'A quantidade de numeros inseridos é')



