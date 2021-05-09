import Listas

try:
    Listas.listas()
except NameError as e:
    print("There is a problem: ", e)
finally:
    print("program end.")
