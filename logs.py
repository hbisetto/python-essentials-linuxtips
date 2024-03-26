#!/usr/bin/env python3

import os
import logging
from logging import handlers

# TODO: usar função
# TODO: usar lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instância de log
log = logging.Logger("logs.py", log_level)
# level
# ch = logging.StreamHandler() # Console/terminal/stderr
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=10**6,  # costuma-se usar maxBytes=10**6 , que é igual a 1MB
    backupCount=10
)
fh.setLevel(log.level)
# formatação
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
# destino
log.addHandler(fh)


# logging  root logger
"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que não afeta uma única execução")
log.critical("Erro geral ex: o banco de dados sumiu")
"""


try: 
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s ", str(e))
    
