
import sys
x = int(input("Informe um número inteiro de até 4 digitos: "))
if(x >= 0 and x <= 9999):
    print(x//1000)               #algarismo 1
    print(x//100-((x//1000)*10)) #algarismo 2
    print(x//10-((x//100)*10))   #algarismo 3
    print(x - ((x//10)*10))      #algarismo 4
    print(f'A soma dos algarismos é: {(x//1000)+ (x//100-((x//1000)*10)) + (x//10-((x//100)*10)) + (x - ((x//10)*10))}')
    sys.exit()
print('Número invalido')