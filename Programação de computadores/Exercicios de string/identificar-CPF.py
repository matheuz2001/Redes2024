import sys
x = input("Informe um CPF(apenas números): ")
aux = 0
#print(len(x))
if(len(x)<11 or len(x)>11):
    sys.exit("Este não é o tamanho de um cpf!")

#Validação do primeiro digito
for i in range(len(x)-2):
    aux += int(x[i]) * (10-i)
if (int(x[9]) == (aux * 10) % 11):
    digito1 = True
#Validação do segundo digito
aux = 0
for i in range(len(x)-1):
    aux += int(x[i]) * (11-i)
if (int(x[10]) == (aux * 10) % 11):
    digito2 = True

    
if(digito1 and digito2):
    print("CPF Válido")