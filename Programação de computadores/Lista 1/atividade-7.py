import sys
import math
a = float(input("informe o lado 'a' do triangulo: "))
b = float(input("informe o lado 'b' do triangulo: "))
c = float(input("informe o lado 'c' do triangulo: "))
if(b>c and not (b-c < a < b+c)):
    print("As linhas formam não formam um triangulo.")
    sys.exit()
elif(not (c-b < a < b+c)):
    print("As linhas formam não formam um triangulo.")
    sys.exit()
elif(a>c and not (a-c < b < a+c)):
    print("As linhas formam não formam um triangulo.")
    sys.exit()
elif(not (c-a < b < a+c)):
    print("As linhas formam não formam um triangulo.")
    sys.exit()
elif(b>a and not (b-a < c < a+b)):
    print("As linhas formam não formam um triangulo.")
    sys.exit()
elif(not (a-b < c < a+b)):
    print("As linhas formam não formam um triangulo.")
    sys.exit()

if(a == b and a == c and b == c):
    print("Triangulo equilátero")
elif(a == b or a == c or b == c):
    print("Triangulo isóceles")
else:
    print("Triangulo escaleno")

cosalpha = (pow(a,2) - pow(b,2) - pow(c,2))/(-2*b*c)
cosbeta = (pow(b,2) - pow(a,2) - pow(c,2))/(-2*a*c)
cosgamma = (pow(c,2) - pow(b,2) - pow(a,2))/(-2*a*b)
angalpha = math.degrees(math.acos(cosalpha))
angbeta = math.degrees(math.acos(cosbeta))
anggamma = math.degrees(math.acos(cosgamma))
if(angalpha == 90):
    print("Angulo alfa, angulo oposto a linha 'a' é um angulo reto")
elif(angalpha < 90):
    print("Angulo alfa, angulo oposto a linha 'a' é um angulo agudo")
else:
    print("Angulo alfa, angulo oposto a linha 'a' é um angulo obtuso")
print(angalpha)
if(angbeta == 90):
    print("Angulo beta, angulo oposto a linha 'b' é um angulo reto")
elif(angbeta < 90):
    print("Angulo alfa, angulo oposto a linha 'b' é um angulo agudo")
else:
    print("Angulo alfa, angulo oposto a linha 'b' é um angulo obtuso")
print(angbeta)
if(anggamma == 90):
    print("Angulo gamma, angulo oposto a linha 'c' é um angulo reto")
elif(anggamma < 90):
    print("Angulo gamma, angulo oposto a linha 'c' é um angulo agudo")
else:
    print("Angulo gamma, angulo oposto a linha 'c' é um angulo obtuso")
print(anggamma)

