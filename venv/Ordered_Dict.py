"""
Módulo Collections: Ordered Dict
Dicionário com ordem de inserção

"""
from collections import OrderedDict

dicionario = {'a': 1, 'b': 23, 'c': 3, 'd': 41, 'e': 5}
for chave, valor in dicionario.items():
    print(f'chaves {chave}:valor={valor}')

dicionario2 = OrderedDict({'a': 1, 'b': 23, 'c': 3, 'd': 41, 'e': 5})
for chave, valor in dicionario2.items():
    print(f'chaves {chave}:valor={valor}')