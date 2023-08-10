#! /usr/bin/env python3
"""
Imprime a tabuada do 1 ao 10.
Tabuada do 1
1
2
3
...
______________
Tabuada do 2
2
4
6
...
_____________
Tabuada do 10
10
20
30
...
"""
__version__ = "0.1.0"
__author__ = "Henrique Bisetto"

# base = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11)) # sempre um número a mais

# Iterable (percorriveis)

for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-" * numero)
