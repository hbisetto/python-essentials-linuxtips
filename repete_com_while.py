#!/usr/bin/env python3

# While - Enquanto
# Quando usar While, sempre tomar cuidado para não criar um loop infinito
n = 0

while n < 101:
    if n == 40:
#        break   break para o programa aqui nessa repetição
        n += 1    # se atentar para colocar este incremento quando usar continue
        continue  # continue ignora esta chamada do loop e começa outra.
    print(n)
    n += 1
