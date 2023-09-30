
numeros = []


while True:
     numero = int(input("Digite um número (ou 0 para encerrar): "))
     if numero == 0:
        break
     numeros.append(numero)


if numeros:
    # Imprime a soma dos números
    print(f"Soma dos números: {sum(numeros)}")

    # Imprime a multiplicação dos números
    resultado_multiplicacao = 1
    for num in numeros:
        resultado_multiplicacao *= num
    print(f"Multiplicação dos números: {resultado_multiplicacao}")

    # Imprime o maior e o menor número
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")
else:
    print("Nenhum número foi digitado.")
