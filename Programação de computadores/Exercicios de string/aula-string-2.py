var1 = "Natal/RN"
var2 = "Rio Grande Do Norte"
#var2 = "arara"
var3 = 352437
aux = str(var3)

#for i in range(0, len(var2)+1):
#    print(var2[0:i])

#for i in range(len(var2),0,-1):
#    print(var2[0:i])

#i=0
#while i <= len(var1):
#    print(var1[0:i])
#    i += 1

#i=len(var1)
#while i >= 0:
#    print(var1[0:i])
#    i -= 1

x=""
#for i in range(len(var2)-1,-1,-1):
#    x+=var2[i]

i=len(var2)-1
while i >= 0:
    x+=var2[i]
    i -= 1

if(x == var2):
    print("Palindromo")
else:
    print("Não palindromo")

