#! /usr/bin/env python3
"""
Script usando interpolação

"""

__version__ = "0.1.0"
__author__ = "Henrique Bisetto"

email_tmpl = """
  Olá, %(nome)s
   
  Tem interesse em comprar %(produto)s?
   
  Este produto é ótimo para resolver 
  %(texto)s
   
  Clique agora em %(link)s
  Apenas %(quantidade)d disponíveis!
   
  Preço promocional %(preco).2f 
  """
clientes = ["Henrique", "João", "Maria"]
for cliente in clientes:
    print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto": "Escrever muito bem", "link": "https://canetaslegais.com", "quantidade": 1, "preco": 50.5 })
