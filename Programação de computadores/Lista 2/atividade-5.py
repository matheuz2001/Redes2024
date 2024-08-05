x = int(input("Informe um número: "))
n = 10
contador = 1
while n < x:
    n *= 10
    contador += 1
print(f"O Número {x} tem {contador} digitos")