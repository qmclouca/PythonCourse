"""
Módulo Collections - Named Tuple

tupla = (1, 2, 3)

named_tuple => São tuplas que possuem nome e parâmetros
"""
from collections import namedtuple
#Forma 1 - declarar a tupla cachorro com três variáveis idade raca nome
cachorro1 = namedtuple('cachorro', 'idade raca nome')
#Forma 2
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')
#Forma 3
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro1(idade=1, raca='Chow-chow', nome='Ray')
print(ray)
print(f'idade de {ray.nome}: {ray.idade}')
tita = cachorro2(idade=2, raca='Doberman', nome='Tita')
print(tita)
print(f'idade de {tita[2]}: {ray[1]}')
jimy = cachorro3(idade=3, raca='Golden Retrivier', nome='Jimy')
print(jimy)
print(f'idade de {jimy.nome}: {jimy.idade}')