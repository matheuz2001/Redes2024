import sys
n1 = int(input("Número 1 que seja positivo e inteiro: "))
n2 = int(input("Número 2 que seja positivo e inteiro: "))
if(n1 < 0 or n2 < 0):
    sys.exit("Um dos números não corresponde!")
while (n2 != 0):
    r = n1 % n2
    n1 = n2
    n2 = r
print(n1)