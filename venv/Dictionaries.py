"""
    funcinonam como os mapas em outras linguagens
    são coleções do tipo chave-valor
    são representados por {chaves}
    chaves e valores podem ser de qualquer tipo
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