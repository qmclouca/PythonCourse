#padrão snake case, parâmetros de entrada separados por, e opcionais

def funtion_1(y):
    x = (y+1)/2
    print(x)

def quadrado(y):
    return y*y

def quadrado_cubo(y):
    return (y*y, y*y*y)

def valor_e_quadrado(y):
    yield y
    yield (y*y*y)


y=3
funtion_1(y)
print(quadrado(y))
print(quadrado_cubo(y))

val_quad = valor_e_quadrado(y)
print(list(val_quad))

"""
para retornar dados podem ser usadas 3 técnicas
return variável   interrompe o fluxo da função e retorna a variável
return (variável1, variável2)    interrompe o fluxo da função e retorna na forma de uma tupla
yield variável     o yield não interrompe o fluxo do programa e permite mais de um return
"""