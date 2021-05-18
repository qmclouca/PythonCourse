"""
Módulo Collections - Counter

Collections -> High performance container Datatypes

Counter - Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário
, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento
"""
# Utilizando o Counter
from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

result = Counter(lista)
print(type(result))
print(result)
"""
result
<class 'collections.Counter'>
Counter({3: 6, 1: 5, 5: 5, 2: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
"""
print(Counter("Rodolfo Lucas Bortoluzzi"))
"""
Counter({'o': 5, 'l': 2, ' ': 2, 'u': 2, 'z': 2, 'R': 1, 'd': 1, 'f': 1, 'L': 1, 'c': 1, 'a': 1, 's': 1, 'B': 1, 'r': 1, 't': 1, 'i': 1})
"""