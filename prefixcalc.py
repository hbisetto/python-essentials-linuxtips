#!/usr/bin/env python3
""" Calculadore prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys
import logging
import os

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)


arguments =  sys.argv[1:]

if not arguments:
    operation = input('operação: ')
    n1 = input('n1: ')
    n2 = input('n2: ')
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print('Número de argumentos inválido')
    print('ex: "sum 5 5"')
    sys.exit(1) # 0 = não teve erro; qualquer número > 0, significa que teve erro.


operation, *nums = arguments

valid_operations = ('sum', 'sub', 'mul', 'div')

if operation not in valid_operations:
    log.error(
        "Operação inválida. \n"
        "%s", valid_operations
    )
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try: 
    n1, n2 = validated_nums #unpack 
except ValueError as e:
    print(str(e))
    sys.exit(1)

# TODO: Usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado é {result}")


