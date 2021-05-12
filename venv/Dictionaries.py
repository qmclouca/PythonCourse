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
    print(paises.get('ru')) # Não causa erro e por isso é preferida

