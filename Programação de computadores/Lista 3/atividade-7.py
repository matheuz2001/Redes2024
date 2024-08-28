import os
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)

lerArquivo = open(dirArquivos + '\\alunos_ifrn.csv','r',encoding='utf-8')
lerArquivo.readline()

#A). Quantia em porcentagem de alunos em cada campus
alunos = [i.split(';')[-1].replace('\n','') for i in lerArquivo]
contagem = [[v, alunos.count(v)] for v in set(alunos)]
contagem.sort(key=lambda x: x[1])

somatorio = sum(int(s[1]) for s in contagem)-1
porcentagem_de_alunos = [(s[0],(s[1]/somatorio)*100) for s in contagem]
#Escrita em arquivo
sairArquivo = open(dirArquivos + '\\alunos_ifrn_campus.csv','w',encoding='utf-8')
for x in porcentagem_de_alunos:
    sairArquivo.write(f'{x[0]};;{x[1]:.2f}%;;\n')
    print(f'{x[0]}: {x[1]:.2f}%')
sairArquivo.close()


lerArquivo = open(dirArquivos + '\\alunos_ifrn.csv','r',encoding='utf-8')
lerArquivo.readline()


#B). Ano de ingresso de cada aluno
anos = [str(i.split(';')[7][0])+str(i.split(';')[7][1])+str(i.split(';')[7][2])+str(i.split(';')[7][3]) for i in lerArquivo]
contagem = [[v, anos.count(v)] for v in set(anos)]
contagem.sort(key=lambda x: x[1],reverse=True)
#Escrita em arquivo
sairArquivo = open(dirArquivos + '\\alunos_ifrn_ano.csv','w',encoding='utf-8')
for x in contagem:
    sairArquivo.write(f'{x[0]};{x[1]};;\n')
    print(f'{x[0]}: {x[1]}')
sairArquivo.close()

#C). Alunos e cursos
lerArquivo = open(dirArquivos + '\\alunos_ifrn.csv','r',encoding='utf-8')
lerArquivo.readline()
cursos = [[i.split(';')[-1].replace('\n',''),i.split(';')[5]] for i in lerArquivo]
instituições = [i[0] for i in cursos]
for x in set(instituições):
    print(f'{x},',end='')
print()
Escolhcamp = input('Escolha o campus: ').upper()

cursos_filtrados = list(filter(lambda x: x[0] == Escolhcamp, cursos))

cursos_do_campus = [x[1] for x in cursos_filtrados]

cursos_unicos = set(cursos_do_campus)

sairArquivo = open(dirArquivos + '\\alunos_ifrn_campus_curso.csv','w',encoding='utf-8')
for curso in cursos_unicos:
    quantidade = cursos_do_campus.count(curso)
    sairArquivo.write(f"{Escolhcamp};;{curso};;{quantidade}Alunos;;\n")
    print(f"{Escolhcamp};;{curso};;{quantidade}Alunos;;\n")
sairArquivo.close()

lerArquivo.close()