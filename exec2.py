def compara_strings():

    string1 = input("Digite a primeira string: ")
    string2 = input("Digite a segunda string: ")


    print("\nConteúdo da primeira string:", string1)
    print("Conteúdo da segunda string:", string2)


    if len(string1) == len(string2):
        if string1 == string2:
            print("As strings têm o mesmo comprimento e são iguais.")
        else:
            print("As strings têm o mesmo comprimento, mas são diferentes.")
    else:
        print("As strings são diferentes.")

'''def imprime_vertical(nome):
    for letra in nome:
        print(letra)


nome = input("Digite seu nome: ")'''



'''def imprime_invertido(nome):

    print(nome[::-1])


while True:

    nome_usuario = input("Digite um nome em maiúsculas: ")


    if nome_usuario.isupper():

        imprime_invertido(nome_usuario)
        break
    else:
        print("Por favor, insira um nome em maiúsculas.")'''


'''def imprime_escada_vertical(nome):
    for i in range(len(nome)):
        print(nome[:i+1])

# Solicita um nome ao usuário
nome_usuario = input("Digite um nome: ")'''

'''nome = input("Entre com o nome")
vazio1=""
vazio2=""
for letra in nome:
    vazio1+=letra
for i in range(len(nome)):
    vazio2=vazio1[0:len(nome)-i]
    print(vazio2)'''


'''lista_original = []


while True:
    numero = int(input("Digite um número (digite 0 para parar): "))
    if numero == 0:
        break
    lista_original.append(numero)


lista_multiplicada = [valor * 3 for valor in lista_original]


print("\nLista original:", lista_original)
print("Lista multiplicada por 3:", lista_multiplicada)'''





'''lista_valores = list(range(1, 11))
print("Valores de 1 a 10:", lista_valores)



frase = input("Digite uma frase: ")
contagem_a = 0
for caractere in frase:
    
    if caractere.lower() == 'a':
        contagem_a += 1

# Imprime o resultado
print(f"A frase possui {contagem_a} letra(s) 'a'.")'''
'''def calcular_tabuada(numero, limite):
    """
    Calcula a tabuada de um número até um determinado limite.

    Parâmetros:
    - numero: O número para o qual a tabuada será calculada.
    - limite: O limite superior para a tabuada.

    Retorna:
    - Uma lista com os resultados da tabuada.
    """
    tabuada = []
    for i in range(1, limite + 1):
        resultado = numero * i
        tabuada.append(resultado)
    return tabuada

# Solicita ao usuário o número para o qual deseja calcular a tabuada
numero_tabuada = int(input("Digite um número para calcular a tabuada: "))

# Solicita ao usuário o limite superior para a tabuada
limite_tabuada = int(input("Digite o limite superior para a tabuada: "))

# Chama a função e obtém a tabuada
resultado_tabuada = calcular_tabuada(numero_tabuada, limite_tabuada)

# Imprime a tabuada
print(f"Tabuada de {numero_tabuada} até {limite_tabuada}: {resultado_tabuada}")'''




