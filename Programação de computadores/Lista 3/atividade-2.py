Listsize = int(input("Quantia de elementos da lista: "))
lista = list()
n = int
while(n != 0):
    n = int(input("Elemento para a lista: "))
    if(len(lista) < Listsize and n!=0):
        lista.append(n)
    elif(n != 0):
        lista.sort(reverse=True)
        lista[0] = n
    lista.sort()
    print(lista)
