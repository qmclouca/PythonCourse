import Listas
import Tuplas
import Dictionaries
import Conjuntos


try:
    #Listas.listas()
    #Tuplas.tuples()
    #Dictionaries.dictionaries()
    Conjuntos.conjuntos()


except NameError as e:
    print("There is a problem: ", e)
finally:
    print("program end.")
