#! /usr/bin/env python3
"""
Imprime a tabuada do 1 ao 10.
---Tabuada do 1---
    1 x 1 = 1
    1 x 2 = 2 
    3 x 1 = 3
...
####################
---Tabuada do 2---
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
...
####################_
"""
__version__ = "0.1.1"
__author__ = "Henrique Bisetto"

numeros = list(range(1,11)) # sempre um número a mais

# Iterable (percorriveis)

for n1 in numeros:
    print("{:^18}".format(f"\U0001F522 Tabuada do {n1} \U0001F522"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}")) 
    print("#" * 18)                
        
