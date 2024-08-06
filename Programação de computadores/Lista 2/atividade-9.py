num = int(input("Enter number:"))
#Salvar número para mais tarde
reserva = num
q_digit= 0
while num > 0:
    num //= 10
    q_digit+=1
#Reiniciar contagem e número
s = 0
num = reserva
while num > 0:
    digit = num % 10
    num //= 10
    s += digit ** q_digit
if s == reserva:
    print(f"{reserva} é um número de armstrong")
else:
    print(f"{reserva} não é um número de armstrong")