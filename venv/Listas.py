"""
Listas em python funcionam como arrays e são dinâmicas
podendo ser usadas com qualquer tipo de dado
    -Não possuem tamanho fixo
    -Não possuem tipo de dado fixo mas usa apenas um tipo em cada tempo
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

