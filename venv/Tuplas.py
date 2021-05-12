"""
Tuplas são listas imutáveis representadas pelo uso de (parênteses)
Apesar de serem imutáveis podem ser sobrescritas
Tuplas precisam ter mais de um elemento
operações em tuplas geram novas tuplas
Não existem métodos de adição e remoção de elementos
Tuplas são mais rápidas do que listas
"""


def tuples():
    tupla1 = (1, 2, 3, 4, 5, 6)
    print(tupla1)
    print(type(tupla1))
    #gerar tuplas com a função range
    tupla2 = tuple(range(2,10,3)) # gerar no intervalo de 2 a 10 com passo 3
    print(tupla2)
    #Desempacotamento de tuplas
    tupla3 = ['Rodolfo', 'Lucas', 'Bortoluzzi']
    first_name, middle_name, last_name = tupla3
    print(first_name)
    print(middle_name)
    print(last_name)
    print(f'Soma dos elementos da tupla1: {sum(tupla1)}')
    print(f'Maior elemento da tupla1: {max(tupla1)}')
    print(f'Menor elemento da tupla1: {min(tupla1)}')
    print(f'Tamanho da tupla1: {len(tupla1)}')
    #concatenação de tuplas
    tupla4 = tupla1 + tupla2
    print(tupla4)
    #verificar se um elemento está em uma tupla
    print(3 in tupla1)
    #iterando
    for n in tupla1:
        print(n)

    for indice, valor in enumerate(tupla1):
        print(indice, valor)

    #contando elementos em uma tupla
    print(tupla4)
    print(tupla4.count(2))

