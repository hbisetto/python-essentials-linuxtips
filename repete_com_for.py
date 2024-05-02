#!/usr/bin/env python3

# For loops / Laço for
print("Exemplo 1:")
print()
dados = {}

for line in open("post.txt"):
    if line == "---\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()

print(dados)

print("* " * 50)

print()
print("Exemplo 2:")
print()

original = [1, 2, 3]
dobrada = []

for n in original:
    dobrada.append(n * 2)

print(dobrada)

# Funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)


# Outro exemplo de List comprehension
# dados = [line for line in open("post.txt") if ":" in line]
# print(dados)

# Dict comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()       # key: value
    for line in open("post.txt")                         # para cada linha
    if ":" in line                                       # se tiver ":" na linha
}

# Poderia fazer o exemplo acima assim:
# dados = {}
# for line in open("post.txt")
#    if ":" in line:
#        key, valor = line.split(":")
#        dados[key] = valor.strip()

print(dados)
