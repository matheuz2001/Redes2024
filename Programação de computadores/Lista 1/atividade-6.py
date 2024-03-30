import sys
from datetime import *
from dateutil.relativedelta import relativedelta
SEXO = input("Informe o sexo: ")
if(SEXO != 'M' and SEXO != 'm' and SEXO != 'F' and SEXO != 'f'):
    print("Sexo invalido")
    sys.exit()
dt_nasc = input('Informe a idade do contribuinte DD/MM/AAAA: ')
dt_nasc = datetime.strptime(dt_nasc, '%d/%m/%Y').date()
dt_de_contr = input('Informe a idade que iniciou a contribuir: ')
dt_de_contr = datetime.strptime(dt_de_contr, '%d/%m/%Y').date()
dt_atual = date.today()

dif_data = relativedelta(dt_atual, dt_nasc)
anos_i = dif_data.years
meses_i = dif_data.months
dias_i = dif_data.days
dif_data = relativedelta(dt_atual, dt_de_contr)
anos_c = dif_data.years
meses_c = dif_data.months
dias_c = dif_data.days

print(f'{dias_i}, {meses_i}, {anos_i}')
print(f'{dias_c}, {meses_c}, {anos_c}')

if(SEXO == 'M' or SEXO == 'm' and anos_c >=35 or anos_i >= 65 and anos_c >= 15):
    print("O individuo pode já se aposentar")
elif(SEXO == 'F' or SEXO == 'f' and anos_c >=30 or anos_i >= 62 and anos_c >= 15):
    print("O individuo pode já se aposentar")