import sys
x = int(input("Tempo em minutos estacionado: "))
TP = 30.00
#TP total a pagar
#xP Tempo parcial
if(x//60 >= 12):
    print(f'o Carro passou {x//60} horas e tem de pagar {TP} reais no total')
    sys.exit()
TP = 0
if(x/60 < 3):
    TP += 8.00 * (x//60)
    if(x/60 - x//60 > 0):
        TP += 8.00
elif(x/60 < 5):
    TP += (8.00 * 2) + 5.00 * ((x//60) - 2)
    if(x/60 - x//60 > 0):
        TP += 5.00
else:
    TP += (8.00 * 2) + (5.00 * 2) + (3.00 * ((x//60) - 4))
    if(x/60 - x//60 > 0):
        TP += 3.00
print(f'o Carro passou {x//60} horas e tem de pagar {TP} reais no total')
sys.exit()


