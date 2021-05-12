import Listas
import Tuplas

try:
    Listas.listas()
    Tuplas.tuples()
except NameError as e:
    print("There is a problem: ", e)
finally:
    print("program end.")
