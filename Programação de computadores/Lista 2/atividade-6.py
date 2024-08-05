import sys
x = float(input("Informe um número para o quociente: "))
y = float(input("Informe um número para a função: "))
q = int(input("Informe um número para a quantia de valores: "))
if(q < 1):
    sys.exit("Este número é menor que 1")
somatorio = x
xinicial = x
for i in range(q):
    x *= y
    somatorio += x
    print(f"Número {i+1}: {x}")
print(f"O somatório da um total de: {somatorio}")

if(y==1):
    print("A Função é Constante")
elif(y < 0):
    print("A Função é Oscilante")
elif(y < 1):
    print("A Função é Decrescente")
else:
    print("A Função é Crescente")

q = int(input("Informe um número para a enésima posição: "))
x = xinicial
for i in range(q):
    x *= y
print(f"O Número na posição {q} é: {x}")