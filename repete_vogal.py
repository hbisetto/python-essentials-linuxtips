"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e 
imprime cada uma das palavras com suas vogais duplicadas.

ex:
$ python3 repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Henrique
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Heenriiquuee

"""
continuar = True
lista = []

while continuar:
    

    palavra = input('Digite uma palavra (ou enter para sair): ')

    if not palavra:
        continuar = False
    else:
        lista.append(palavra)
    
for item in lista:
    print(item)
