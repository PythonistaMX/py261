#! /usr/bin/env python

def mult(x:int, y:float=1.5) -> float:
    ''''Define a una función que multiplica a un entero  y un número.'''
    return x * y
print(f'Despliega mult(2): {mult(2)}')
print(f'Despliega mult(2, 3.14): {mult(2, 3.14)}')
print(f'Despliega mult(2, \'2\'): {mult(2, "2")}') # No cumple con el tipado.