n = int(input("Escolha um número inteiro: "))
x = 1
while x <= n:
    if(n == x*(x+1)/2):
        print("É um número triangular")
        break
    x+=1
    