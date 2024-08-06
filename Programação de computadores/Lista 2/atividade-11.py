import sys

#U - Cima
#D - Baixo
#R - Direita
#L - Esquerda

#O - Noroeste
#N - Nordeste
#E - Sudeste
#W - Sudoeste

x = int(input("Onde em X está o robo?: "))
y = int(input("Onde em Y está o robo?: "))
inicialx = x
inicialy = y
q_move = 0
moveu = False
print("Digite sair, para terminar")
while True:
    print("Movimentação: U:↑, D:↓, R:→, L:←, O:↖, N:↗, E:↘, W:↙")
    move = input("Escolha uma direção para se movimentar: ")
    if(move.upper() == "U" or move.upper() == "O" or move.upper() == "N"):
        y += 1
        moveu = True
    elif(move.upper() == "D" or move.upper() == "E" or move.upper() == "W"):
        y -= 1
        moveu = True
    if(move.upper() == "R" or move.upper() == "N" or move.upper() == "E"):
        x += 1
        moveu = True
    elif(move.upper() == "L" or move.upper() == "O" or move.upper() == "W"):
        x -= 1
        moveu = True
    elif(move.upper() == "SAIR"):
        break
    else:
        print("Opção invalida")
    if(moveu == True):
        q_move +=1
        moveu = False
print(f"Posição inicial x: {inicialx}")
print(f"Posição inicial y: {inicialy}")
print(f"Ele fez {q_move} movimentos")
print(f"Está em {x} x, {y} y")

if(inicialx>0 and inicialy>0):
    print("Iniciou no primeiro quadrante")
elif(inicialx<0 and inicialy>0):
    print("Iniciou no segundo quadrante")
elif(inicialx<0 and inicialy<0):
    print("Iniciou no terceiro quadrante")
else:
    print("Iniciou no quarto quadrante")
if(x>0 and y>0):
    print("E terminou no primeiro quadrante")
elif(x<0 and y>0):
    print("E terminou no segundo quadrante")
elif(x<0 and y<0):
    print("E terminou no terceiro quadrante")
else:
    print("E terminou no quarto quadrante")
