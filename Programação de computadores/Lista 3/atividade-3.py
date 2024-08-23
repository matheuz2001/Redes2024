import sys
import os
import random
#Recomendação, não utilize 60 vai consumir muitissima RAM
#para o processo (Fiz o teste com 10)
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)

Listsize = int(input("Qual o tamanho da lista?(Escolha entre 7 a 60): "))
if(Listsize > 60 or Listsize < 7):
    sys.exit('Tamanho irregular')
lista = random.sample(range(1,61),Listsize)

salvarN = open(dirArquivos + '\\numeros_escolhidos.txt','w',encoding='utf-8')

for numeros in range(len(lista)):
    salvarN.write(f"{lista[numeros]};")
salvarN.close()

combos = [[]]
for n in lista:
    combos += [combinar + [n] for combinar in combos]
for x in range(len(combos)):
    combos[x].sort()

salvarN = open(dirArquivos + '\\combinações.txt','w',encoding='utf-8')

for linhas in combos:
    for items in range(len(linhas)):
        salvarN.write(f"{linhas[items]};")
    salvarN.write(f"\n")
salvarN.close()