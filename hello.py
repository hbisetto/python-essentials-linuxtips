#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe através do CLI arguments "--lang"

Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py

    Pode-se passar um parâmetro de lang e de count:
        python3 hello.py --lang=es_SP --count=5

    Se não for passado nenhum parâmetro, haverá uma interação pedindo o mesmo.
    
    Ou seja, a cadeia de input está completa, seja por parâmetro ou com interação
    
"""
__version__ = "0.1.3"
__author__ = "Henrique Bisetto"
__license__="Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)


# print(f"{sys.argv=}")  # Exibe os argumentos passados na chamada do programa
                       # f string + objeto que quer imprimir + "="
                       # o sys.argv é uma lista [' ... ']

arguments = {
    "lang": None,  # ou seja, espera receber um argumento do tipo LANG, com default None
    "count": 1 # espera também receber um argumento do tipo count, com default None também
}

for arg in sys.argv[1:]: # Para cada um dos argumentos em sys.argv começando a partir do 1 ("1:")
    # TODO: Logging
    try:        
        key, value = arg.split("=") # separa as informações que foram passadas a.antes do "=" e b. depois do "="
    except ValueError as e:
        log.error(
            "You need to use '=', you passed %s, try --key=value: %s",
            arg,
            str(e) 
        )
        sys.exit(1)
    
    key = key.lstrip("-").strip()  # Para remover os "--" + remover o espaço normal(.strip())
    value = value.strip()
    
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()  # Pára de executar o programa nesta hora 
    arguments[key] = value
    
current_language = arguments["lang"]

if current_language is None:
    # TODO: usar repetição
    
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")
    
current_language = current_language[:5]
    
msg = {
    "en_US": "Hello, World",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"    
}

"""
message = msg.get(current_language, msg["en_US"]) # valor default
"""

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))
