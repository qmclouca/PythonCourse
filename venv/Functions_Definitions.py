"""
padrão snake case, parâmetros de entrada separados por, e opcionais

para retornar dados podem ser usadas 3 técnicas
return variável   interrompe o fluxo da função e retorna a variável
return (variável1, variável2)    interrompe o fluxo da função e retorna na forma de uma tupla
yield variável     o yield não interrompe o fluxo do programa e permite mais de um return


"""
def function_1(y):
    x = (y+1)/2
    print(x)

def quadrado(y):
    return y*y

def quadrado_cubo(y):
    return (y*y, y*y*y) # retorna uma tupla de resultados

def valor_e_quadrado(y):
    yield y
    yield (y*y*y) # retorna uma lista com os yields

def print_nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

"""
standard parameters functions/funções com parâmetros 
opcionais => potencia tem um valor padrão
Em fuções Python, os parâmetros com valores default DEVEM sempre estar ao
final da declaração
na função abaixo numero é um parâmetro obrigatório e potencia é um opcional
"""
def exponencial(numero, potencia=2):
    return numero ** potencia

"""
usar funções como parâmetros
exemplo:
"""
def soma(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mat(num1, num2, function=soma):
    return function(num1, num2)

print(mat(5,6))
print(mat(5,6,sub))

"""
declaração de funções dentro de funções
exemplo:
"""
def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

print(exponencial(2, 8))
print(exponencial(3))
y=3
function_1(y)
print(quadrado(y))
print(quadrado_cubo(y))

val_quad = valor_e_quadrado(y)
print(list(val_quad))
nome='Rodolfo'
sobrenome='Bortoluzzi'
print(print_nome_completo('Rodolfo', 'Bortoluzzi'))
print(print_nome_completo(nome=nome, sobrenome=sobrenome)) # using Keyword Arguments
print(print_nome_completo(nome='Rodolfo', sobrenome='Bortoluzzi')) # using Keyword Arguments
print(print_nome_completo(sobrenome='Bortoluzzi', nome='Rodolfo')) # using Keyword Arguments
