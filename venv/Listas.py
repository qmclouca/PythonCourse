"""
Listas em python funcionam como arrays e são dinâmicas
podendo ser usadas com qualquer tipo de dado
    -Não possuem tamanho fixo
    -Não possuem tipo de dado fixo
    -aceitam repetição de dados
    usam [ ]
"""
#encontrar valor em lista (pode ser qualquer tipo, string, boolean, int, float)
import random


def listas():
    lista1 = [90, 70, 40, 5, 10, 17, 19, 5, 55]
    string_list = ['Rodolfo', 'Lucas', 'Bortoluzzi']
    num = 5
    nome = "Rodolfo"

    #encontrar valores em uma lista
    if num in lista1:
        print(f'O valor {num} está na lista')
    else:
        print(f'O valor {num} não está na lista')
    if "Rodolfo" in string_list:
        print(f'O nome {nome} está na lista')
    else:
        print(f'O nome {nome} não está na lista')

    #ordenar uma lista
    print('Lista: ', *lista1)
    lista1.sort()
    print('Lista ordenada: ', *lista1)
    lista1.reverse()
    print('Lista revertida: ', *lista1)
    print(f'Ocorrências do número 5 na lista: {lista1.count(5)}')
    lista1.pop() #remove e retorna o último elemento da lista
    print('Lista após pop: ', *lista1)
    lista1.append([1, 2, 3])
    print('Lista após append: ', *lista1)
    lista1.pop()
    lista1.extend([1, 2, 3])
    print('Lista após extend: ', *lista1)
    lista1.insert(3, 'Novo_Valor')
    print('Lista após inserção na posição 2 do valor (Novo_Valor): ', *lista1)
    lista3 = lista1 + string_list
    print('Concatenando listas: ', *lista3)
    lista1.pop(3)
    print('Retirando o Novo_valor da lista: ', *lista1)
    print('Usando slice para modificar lista: ', *lista1[5:2:-1])
    print('Usando slice para modificar lista: ', *lista1[1:10:2])
    lista2 = lista1.copy()
    print('lista2 como cópia da lista 1: ', *lista2)
    print('Tamanho da lista2: ', len(lista2))
    print('Limpar a lista2', lista2.clear())
    lista2 = lista1.copy() * 3
    print('Lista2 = lista1 * 3: ', lista2)
    string1 = "Rodolfo Lucas Bortoluzzi"
    string1 = string1.split() #o separador padrão é o espaço entre parenteses colocar o separador ex: ','
    print('Transformar string em lista usando split', string1)
    # transformar uma lista em string usando o separador ' ':
    string1 = ' '.join(string1)
    print('Remontando a string a partir da lista com join(): ', string1)

    # iterando sobre listas
    lista4 = list(range(10))
    soma = 0
    for element in lista4:
        print(f'{element} ', end=" ")
        soma = soma + element
    print('soma: ', soma)

    cores = ['verde', 'amarelo', 'azul', 'branco']
    #Gerar indice em um for
    for indice, cor in enumerate(cores):
        print(indice, cor, end=" ")

    #Encontrar o índice de um elemento em uma lista
    #em qual índice está a primeira ocorrência do valor 70
    print(f'\n O item 70 está no item {lista1.index(70)}')
    #a mesma busca em um range, abaixo procura a primeira ocorrência de 5 a partir do índice 3
    print(f'A primeira ocorrência de 5 após o índice 4 ocorre no índice {lista1.index(5, 4)}')
    #o range pode te posição inicial e final ex: lista1.index(5,4,10) procura 5 entre os índices 4 e 10

    #para usar o slice
    print(f'Cortando a lista do índice 1 ao 5 com passo 2: {lista1[1:5:2]}') #lista[início:fim:passo]

    print('Soma da lista toda: ', sum(lista1))
    print('Maior valor na lista toda: ', max(lista1))
    print('Menor valor na lista toda: ', min(lista1))

    tupla1 = tuple(lista1) #Converter um lista em tupla
    print('Lista 1 transformada em tupla: ', tupla1, f'. Tipo de dado da tupla 1: {type(tupla1)}')

    #Desempacotamento de listas
    lista5 = [1, 3, 5, 6, 7, 19, 40]
    print(lista5)
    num1, num2, num3, num4, num5, num6, num7 = lista5
    print(num1,', ', num2,', ', num3, ', ',num4, ', ',num5, ', ',num6, ', ', num7)

    #Copiando uma lista para outra (Shallow copy e Deep copy)
    #Deep copy após a cópia modificações na lista original não afetam a cópia
    lista6 = [1, 2, 3]
    print(lista6)
    novaLista = lista6.copy()
    print(novaLista)
    novaLista.append(4)
    print(lista6)
    print(novaLista)
    #Shallow copy após a cópia modificações na lista original também afetam a cópia
    lista6 = [1, 2, 3]
    print(lista6)
    novaLista = lista6
    print(novaLista)
    novaLista.append(4)
    print(lista6)
    print(novaLista)



