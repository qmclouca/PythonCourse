import Listas
import Tuplas
import Dictionaries

try:

    #Listas.listas()
    #Tuplas.tuples()

    Dictionaries.dictionaries()
except NameError as e:
    print("There is a problem: ", e)
finally:
    print("program end.")
