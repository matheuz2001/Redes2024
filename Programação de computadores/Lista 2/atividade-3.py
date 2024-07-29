n = int(input("Digite a quantia de primos"))
for i in range(2, n):
    primo = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(f"{i} é um número primo")