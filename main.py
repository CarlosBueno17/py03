'''def Soma(x,y):
    return x+y

def Sub(x,y):
  return -y

def Mult(x, y):
  return x* y

def dividir(x, y):
   return x/ y


valor1 = float(input("Entre com valor 1 : "))
operacao = input("Digite a operação desejada")
valor2 = float(input("Entre com valor 2 : "))


if operacao == "+":
    print(Soma(valor1, valor2))
elif operacao == "-":
    print(Sub(valor1, valor2))
elif operacao == "*":
    print(Mult(valor1, valor2))
elif operacao == "/":
    print(dividir(valor1, valor2))
else:
    print("opção invalida")'''




'''def pessoas(**kwargs):
    print(kwargs)
    for nome,idade in kwargs.items():
        print(f'{nome} tem atualmente {idade} anos de idade')

pessoas(gabriel='33',rafael='45',daniel='33')'''




'''def a (x):
    return x **2
print(a(4))
b=lambda x:x**2
print(b(4))
s=lambda x,y:x+y
print(s(2,3))'''



lista=[4,5,6,7,8]
print(lista)

lista.append(2)
print(list)

lista.insert(2,-3)
print(lista)

lista.remove(4)
print(lista)

lista2 =[10,5,7,6,1,3,2,70]
lista2.sort()

print(lista2)

lista2.reverse()
print(lista2)

lista3=[2,3,4,5,7,5,9,5]
qnt=lista3.count(5)
print(qnt)

lista4=[1,2,3,4,5,6,7,8,9]
exc=lista4.pop()
print(exc)

lista5=[1,2,3,4,5,6,7,8,9,10]
lista5.pop()
print(lista5)

lista6=[1,2,3,4,5]
del lista6[2]
print(lista6)

lista7=[2,4,5,8,10,12]
del lista7[2:5]


