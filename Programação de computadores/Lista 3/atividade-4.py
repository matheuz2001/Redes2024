import random
import sys
#import statistics
n = int(input("Qual o tamanho da lista?: "))
if(n <= 0):
    sys.exit("Número menor que 0")
lista = [random.randint(0,100) for x in range(n)]
media = 0
mediana = 0
for i in range(len(lista)):
    media += lista[i]
media = media/len(lista)

#Lista auxiliar
lauxi = lista
lauxi.sort()

print(len(lista)%2)

if(len(lista)%2 != 0):
    mediana = lauxi[int(len(lista)/2)]
else:
    mediana = (lauxi[int(len(lista)/2)] + lauxi[int(len(lista)/2)-1])/2

varia = sum([(lista[x] - media) ** 2 / len(lista) for x in range(len(lista))])

print(f'Números da lista: {lista}')
print(f'Media: {media}')
#print(statistics.mean(lista))
print(f'Mediana: {mediana}')
#print(statistics.median(lista))
print(f'Variância populacional: {varia}')
#print(statistics.pvariance(lista))
print(f'Desvio padrão populacional: {varia**(1/2)}')
#print(statistics.pstdev(lista))

