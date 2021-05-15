"""
Usa teoria de conjuntos
Conjuntos são Sets
Sets não possuem valores duplicados
Sets não possuem valores ordenados
Elementos não são acessados via índice, ou seja, não são indexados
Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles
Quando não há preocupação com chaves, valores ou itens duplicados
Os conjuntos são referenciados em Python com chaves {}
Podem ser misturados tipos de dados
Diferença entre conjuntos (set) e mapas (dicionários) em Python:
    - Dicionário possue chave e valore
    - Conjuntos possuem apenas valores
"""
def conjuntos():
    #definindo um conjunto:
    # Forma 1
    s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) #Valores repetidos serão ignorados
    print(s)
    print(type(s))
    # Forma 2
    s1 = {1, 2, 3, 4, 5, 5} # Valores duplicados são ignorados
    print(s1)
    print(type(s1))
    # Uso do set para converter listas letras que se repetem são ignoradas
    nome = 'Rodolfo Lucas Bortoluzzi'
    set_nome = set(nome)
    print(set_nome)
    #iterar
    for valor in s:
        print(valor, end=" ")

    # verificar valor no set
    if 3 in s:
        print('\nTem o 3')
    else:
        print('Não tem o 3')
    # diferenças entre outras coleções de dados e os conjuntos


    lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
    print(f'Lista: {lista} com {len(lista)} elementos')

    tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
    print(f'Tupla: {tupla} com {len(tupla)} elementos')

    dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
    print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

    conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
    print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

    #adicionando elementos
    print(s)
    s.add(37)
    print(s)
    #removendo elementos
    s.pop() #retira o primeiro elemento do conjunto
    print(s)
    s.remove(3) #remove o valor 3
    print(s)
    s.discard(2) #se o valor não for encontrado não será gerado erro
    print(s)

    #Deep copy cria conjuntos independentes aloca novo espaço em memória para a nova variável
    novo_conjunto = s.copy()
    print(novo_conjunto)
    novo_conjunto.add(2)
    print(novo_conjunto)
    print(s)
    #Shallow copy cria conjuntos dependentes pois ambas tem o mesmo endereço de memória
    novo_conjunto2 = s
    novo_conjunto2.add(2)
    print(novo_conjunto2)
    print(s)
    #limpar conjunto
    novo_conjunto.clear()
    print(novo_conjunto)
    
    #Métodos matemáticos de conjuntos
    estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
    estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}
    
    #Gerar um conjunto de estudantes unicos
    #Forma 1 - Utilizando union
    unicos1 = estudantes_python.union(estudantes_java)
    print(unicos1)
    #Forma2 - utilizando pipe 
    unicos2 = estudantes_python | estudantes_java
    print(unicos2)

    #Gerar um conjunto de estudantes em ambos os cursos
    #Forma1 - utilizando intersection
    ambos1 = estudantes_python.intersection(estudantes_java)
    print(ambos1)

    #Forma2 - utilizando &
    ambos2 = estudantes_python & estudantes_java
    print(ambos2)

    #Gerar um conjunto de estudantes que estão em um curso e não estão no outro
    so_python = estudantes_python.difference(estudantes_java)
    print(so_python)

    so_java = estudantes_java.difference(estudantes_python)
    print(so_java)

    #Funções comuns com conjuntos
    s = {1, 2, 3, 4, 60, 324, 52345, 43321}
    print(s)
    print(sum(s))
    print(max(s))
    print(min(s))
    print(len(s))

    