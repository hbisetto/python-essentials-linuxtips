#!/usr/bin/env python3

import os
import logging

# TODO: usar função
# TODO: usar lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instância de log
log = logging.Logger("logs.py", log_level)
 
# level
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(log_level)
# formatação
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)


# logging  root logger
"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que não afeta uma única execução")
log.critical("Erro geral ex: o banco de dados sumiu")
"""
print("-" * 30)

try: 
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s ", str(e))
    
