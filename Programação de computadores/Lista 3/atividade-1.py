import random
n1 = int(input("Quantia de Linhas: "))
n2 = int(input("Quantia de Colunas: "))

matriz = [[random.randint(0,10) for lista in range(n2)] for x in range(n1)]
print(matriz)
matriz = [[i[x] for i in matriz]for x in range(n2)]
print(matriz)
