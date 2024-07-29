n = int(input("Digite a quantia de primos"))
count = 0
num = 2  #Primeiro primo

while count < n:
    primo = True
    if num <= 1:
        primo = False
    elif num <= 3:
        primo = True
    elif num % 2 == 0 or num % 3 == 0:
        primo = False
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                primo = False
                break
            i += 6
    if primo:
        print(num)
        count += 1
    num += 1