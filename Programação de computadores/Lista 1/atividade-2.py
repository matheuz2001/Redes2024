x = float(input("Informe um valor positivo: "))
x100 = x//100
x = round(x - (x100*100),2)
x50 = x//50
x = round(x - (x50*50),2)
x20 = x//20
x = round(x - (x20*20),2)
x10 = x//10
x = round(x - (x10*10),2)
x5 = x//5
x = round(x - (x5*5),2)
x2 = x//2
x = round(x - (x2*2),2)
x1 = x//1
x = round(x - x1,2)
x050 = x//0.5
x = round(x - (x050 * 0.5),2)
x025 = x//0.25
x = round(x - (x025 * 0.25),2)
x010 = x//0.10
x = round(x - (x010 * 0.1),2)
x005 = x//0.05
x = round(x - (x005 * 0.05),2)
x001 = x//0.01
print(f'O troco total é de:')
if(x100 > 0):
    print(f'{int(x100)} notas de 100 Reais')
if(x50> 0):
    print(f'{int(x50)} notas de 50 Reais')
if(x20> 0):
    print(f'{int(x20)} notas de 20 Reais')
if(x10> 0):
    print(f'{int(x10)} notas de 10 Reais')
if(x5> 0):
    print(f'{int(x5)} notas de 5 Reais')
if(x2> 0):
    print(f'{int(x2)} notas de 2 Reais')
if(x1> 0):
    print(f'{int(x1)} notas de 1 Real')
if(x050> 0):
    print(f'{int(x050)} moedas de 50 Centavos')
if(x025> 0):
    print(f'{int(x025)} moedas de 25 Centavos')
if(x010 > 0):
    print(f'{int(x010)} moedas de 10 Centavos')
if(x005 > 0):
    print(f'{int(x005)} moedas de 5 Centavos')
if(x001 > 0):
    print(f'{int(x001)} moedas de 1 Centavos')