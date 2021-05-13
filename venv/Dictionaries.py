"""
    funcinonam como os mapas em outras linguagens
    são coleções do tipo chave-valor
    são representados por {chaves}
    chaves e valores podem ser de qualquer tipo
    as chaves não podem ser repetidas
"""


def dictionaries():
    # Forma 1 de criação de dicionários
    paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
    print(paises)

    # Forma 2 de criação de  dicionários
    paises1 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
    print(paises1)

    #Acessar via chave
    print(paises['br'])

    #Acessar via get
    print(paises.get('br'))
    print(paises.get('ru')) # Não causa erro e por isso é preferida no caso de não encontrar o valor para a chave retorna None

    #Verificar a ocorrencia de uma chave ou objeto no dicionário
    print(f'A chave br está no dicionário? ', 'br' in paises)
    print(f'O objeto Estados Unidos está no dicionário? ', "Estados Unidos" in paises1)
    print(f'A chave ru está no dicionário? ', 'ru' in paises)

    #Podem ser utilizados quaisquer tipos de dados (int, float, string, boolean), inclusive listas, tuplas, dicionários como chaves
    localidades = {
        (35.6895, 39.6917): 'Escritório de Tókio',
        (40.7128, 74.0060): 'Escritório de Nova York',
        (37.7749, 122.4194): 'Escritório de São Paulo'
    }
    print(localidades)
    print(localidades.get((40.7128, 74.0060)))
    # Adicionar elementos em um dicionário
    receita = {'jan': 100, 'fev': 120, 'mar': 300}
    # Forma 1
    print(receita)
    receita['abr'] = 350
    print(receita)
    # Forma 2
    receita.update({'mai': 500})
    print(receita)

    #Remover dados de um dicionário
    #Forma 1 é sempre necessário informar a chave caso contrário um KeyError será retornado
    #O pop remove e retorna o valor
    receita_popped = receita.pop('mar')
    print(receita_popped)
    print(receita)
    
    #Forma 2 se a chave não existir será gerado um KeyError
    del receita['fev']
    print(receita)

    #Exemplo1 de utilização um carrinho pode ser feita com lista ou tuplas
    carrinho = []
    produto1 = ['Playstation 4', 1, 2300.00]
    produto2 = ['God of war 4', 1, 150.00]
    carrinho.append(produto1)
    carrinho.append(produto2)
    print(carrinho)
    #usando dicionários ver que fica bem mais detalhado e fácil de identificar cada campo
    carrinho = []
    produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
    produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}
    carrinho.append(produto1)
    carrinho.append(produto2)
    print(carrinho)

    #métodos para dicionários dir({}) => 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

    d = dict(a=1, b=2, c=3)
    print(d)
    #deep copy
    novo = d.copy()
    print(novo)
    novo['d'] = 4
    print(d)
    print(novo)
    #shallow copy
    novo2 = d
    print(novo2)
    novo2['d'] = 4
    print(d)
    print(novo2)
    d.clear()
    print(d)
    #forma não usual de criação de dicionarios
    outro = {}.fromkeys('a','b')
    print(outro)
    usuario = {}.fromkeys(['nome','pontos','email','profile'], 'desconhecido')
    print(usuario)
    stringtest = {}.fromkeys('teste','valor')
    print(stringtest)
    rangetest = {}.fromkeys(range(1,11),'novo')
    print(rangetest)