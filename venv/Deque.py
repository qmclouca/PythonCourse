"""
Módulo Collections - Deque
Podemos dizer que o deque é uma lista de alta performance
"""
from collections import deque

deq = deque('Rodolfo Lucas')
print(deq)
deq.append('Bortoluzzi')
print(deq)
deq.appendleft('Nome: ')
print(deq)
deq.pop()
print(deq)
deq.popleft()
print(deq)
