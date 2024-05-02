"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar endo que caso será exibida uma mensagem de alerta dependendo 
das condições:

temp maior que 45: ALERTA! Perigo de calor extremo
temp vezes 3 for maior ou igual umidade: ALERTA! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: ALERTA: Frio extremo

"""
import sys
import logging 

log = logging.Logger("alerta")

try:
    temp = float(input("Qual a temperatura atual?").strip())
except ValueError:
    log.error("Temperatura inválida")
    sys.exit(1)

try:
    umidade = float(input("Qual a umidade do ar atual?").strip())
except ValueError:
    log.error("Umidade inválida")
    sys.exit(1)


    
    umidade = float(input("Qual  umidade do ar?"))

if temp > 45:
    print("ALERTA! Perigo de calor extremo")
elif (temp * 3) >= umidade:
    print("ALERTA! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp <= 10:
    print("Frio")
elif temp < 0:
    print("Frio extremo")
else:
    print(f"Opções inválidas {temp}, {umidade}")
