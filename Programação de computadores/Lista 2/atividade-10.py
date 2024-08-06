import sys
n = 0
palavra_chave = "Herbalista"
letras_jogadas = ""
while n < 6:
    letra = input(f"Informe uma letra: ")
    if(letra.upper() in letras_jogadas.upper()):
        print(f"A letra {letra} já foi usada")
    elif(letra.upper() in palavra_chave.upper()):
        print(f"Acertou a letra, a palavra tem {letra}")
        for i in range(len(palavra_chave)):
            if(palavra_chave[i].upper() == letra.upper()):
                letras_jogadas += letra
    else:
        print(f"Erro: de número: {n+1}")
        n+=1
    x = "".join(sorted(palavra_chave))
    y = "".join(sorted(letras_jogadas))
    if(x.upper() == y.upper()):
        sys.exit("Fim de jogo, Parabens")
print("Fim de jogo!")