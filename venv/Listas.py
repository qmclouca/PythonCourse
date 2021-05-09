"""
Listas em python funcionam como arrays e são dinâmicas
podendo ser usadas com qualquer tipo de dado
    -Não possuem tamanho fixo
    -Não possuem tipo de dado fixo
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
    lista1.pop()
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