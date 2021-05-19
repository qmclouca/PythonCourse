"""
Módulo Collections - Default dict
Tem todas as funções do Dictionaries

dicionario = {'curso': 'Python completo'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) # causa erro pois a chave não existe

Ao criar um dicionario usando o default dict chaves inexistentes não causam erro
pois existe um valor default (lambda) para isso. Este valor será utilizado sempre que não
houver um valor definido. Caso tentemos acessar uma chave que não existe, essa
chave será criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome, que podem ou nõa receber parâmetros de entrada e
retornar valores
"""
#fazer o import
from collections import defaultdict
dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'programação em python'
print(dicionario)
print(dicionario['outro'])
print(dicionario)
"""
output:
defaultdict(<function <lambda> at 0x0000028E53135280>, {'curso': 'programação em python'})
0
defaultdict(<function <lambda> at 0x0000028E53135280>, {'curso': 'programação em python', 'outro': 0})
"""