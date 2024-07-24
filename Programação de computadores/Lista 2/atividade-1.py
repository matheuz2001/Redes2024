import sys
x = input("Em gramas, qual a massa inicial do material radioativo: ")
tempo = 0 #em segundos
if(not x.isdigit):
    sys.exit("Não é um número")
y=float(x)
while (y >= 0.5):
    y = y/2
    tempo += 50
print("Massa inicial: ",x)
print("Massa Final: ", y)
print("Tempo de Decaimento: ",((tempo-(tempo//60))//60)//60,":",tempo//60,":",tempo%60)
