#! usr/bin/env python3
"""
Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Henrique Bisetto"

atividades = {
    "Ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"],
    "Danca": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

alunos = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

dicionario_final = {
    "Ingles": {"sala1": [], "sala2": []},
    "Musica": {"sala1": [], "sala2": []},
    "Danca": {"sala1": [], "sala2": []}
}

for atividade, alunos_atividade in atividades.items():
    for sala, alunos_sala in alunos.items():
        for aluno in alunos_atividade:
            if aluno in alunos_sala:
                dicionario_final[atividade][sala].append(aluno)

print(dicionario_final)
    
