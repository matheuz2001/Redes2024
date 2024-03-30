import sys
HP = int(input("Em que horas o carro deu partida? "))
MP = int(input("Em que minutos o carro deu partida? "))
HD = int(input("Em que horas o carro chegou no destino? "))
MD = int(input("Em que minutos o carro chegou no destino? "))
SD = int(input("Quanto tempo em segundos se passou em descanso? "))
LG = int(input("Quanto de combustível em litros foi gasto? "))
PC = int(input("Qual o preço em real do litro do combustível? "))
DP = int(input("Em quilômetros, qual a distância percorrida? "))
if(HP < 0 or MP < 0 or HD < 0 or MD < 0 or SD < 0 or LG =< 0 or PC =< 0 or DP =< 0):
    print('Entrada invalida')
    sys.exit
#A). Tempo da viagem (Em segundos)
#TV = Tempo de viagem
if(HP > 24 or HD > 24 or MP > 60 or MD > 60):
    print('Entrada invalida')
    sys.exit
if(MP > MD):
    TV = ((60 - MP) + MD) * 60
    HD -= 1
else:
    TV = (MD - MP) * 60
if(HP > HD):
    TV += (((24 - HP)+HD)*60)*60
else:
    TV += ((HD - HP)*60)*60
print(f'O tempo da viagem em segundos é de {TV}')
#B). Velocidade média (KM/H) global, Velocidade média em movimento (KM/H)
# VM = Velocidade média
# VMM = Velocidade média em movimento
VM = DP//((TV/60)/60)
print(f'O carro se manteve em {int(VM)} Km/h durante a viagem completa')
VMM = DP//(((TV - SD)/60)/60)
print(f'O carro se manteve em {int(VMM)} Km/h durante o movimento')

#C). Custo da viagem com combustível (em R$)
#CB = Custo do combustível
CB = LG * PC
print(f'Foi gasto R$:{CB} em combustível nessa viagem')
#D). Desempenho do carro
# KM/H
# L/h
# R$/KM
print(f'Foi feito {round(DP/LG,2)} quiômetros por litro')
print(f'Se gastou {round(LG/((TV/60)//60),2)} litros por hora')
print(f'Custou {round(CB/DP,2)} Real por quilômetro')
