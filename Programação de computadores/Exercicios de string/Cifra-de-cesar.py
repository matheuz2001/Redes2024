import sys
x = input("Informe uma frase: ")
y = int(input("Informe um número para a cifra: "))
z = ""
#A = 65, Z = 90, a = 97, z = 122
while(y>25):
    y -= 25
for i in range(len(x)):
    if(ord(x[i]) + y >= 65 and ord(x[i]) + y <= 90 or ord(x[i]) + y >= 97 and ord(x[i]) + y <= 122):
        z += chr(ord(x[i]) + y)
    elif(ord(x[i]) + y > 122):
        z += chr(97+y-1)
    elif(ord(x[i]) + y > 90):
        z += chr(65+y-1)        
print(z)
