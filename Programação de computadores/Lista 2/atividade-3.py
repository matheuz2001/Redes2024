n = int(input("Digite a quantia de primos: "))
encontrados = False
num = 2 #Primeiro primo

while not encontrados:
    valor_temp = num
    contador_1 = 0
    contador_2 = 0
    primos_1 = ""
    primos_2 = ""


    i = 2 #Iniciar contagem
    #Encontrar primeiro número e primos
    while i * i <= valor_temp:
        if (valor_temp % i == 0):
            if i != ultimo_primo_encontrado:
                contador_1 += 1
                ultimo_primo_encontrado = i
                primos_1 += str(i) + " * " 
            valor_temp //= i
        else:
            i += 1
    if valor_temp > 1 and valor_temp != ultimo_primo_encontrado:
        contador_1 += 1
        primos_1 += str(valor_temp) #Último valor primo para a listagem

    valor_temp = num + 1
    i = 2 #Reiniciar contagem
    #Encontrar segundo número e primos
    while i * i <= valor_temp:
        if (valor_temp % i == 0):
            if i != ultimo_primo_encontrado:
                contador_2 += 1
                ultimo_primo_encontrado = i
                primos_2 += str(i) + " * "
            valor_temp //= i
        else:
            i += 1
    if valor_temp > 1 and valor_temp != ultimo_primo_encontrado:
        contador_2 += 1
        primos_2 += str(valor_temp) #Último valor primo para a listagem

    if contador_1 == n and contador_2 == n:
        encontrados = True
        #primos_1 = primos_1[:-3] #Remove " * " do final da string
        #primos_2 = primos_2[:-3] #Remove " * " do final da string
        print(f"{num} = {primos_1}")
        print(f"{num + 1} = {primos_2}")
    else:
        num += 1