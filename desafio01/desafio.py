"""Dados os valores de horários, decifre a lógica e faça um código para executar:
entrada01: 3:45
entrada02: 14:20
saída: 6:05"""

""" Dividir horas e minutos para exibição
    *Converter na saída para formato 12h
    *Fazer um if para transformar 24h em 12h
"""

hora1 = int(input("Digite a primeira hora: "))
min1 =  int(input("Digite os minutos: "))

hora2 = int(input("Digite a segunda hora: "))
min2 =  int(input("Digite os minutos: "))

if hora1 == 0:
    hora1 = 24
elif hora2 == 0:
    hora2 = 24

somaH = hora1 + hora2
somaMin = min1 + min2

#Conversão das horas e min pra 12h
if somaMin >= 60:
    somaH += 1
    somaMin -= 60
    if somaMin >= 60:
        somaH +=1
        somaMin = 0

if somaH == 0:
    somaH = 12
elif somaH > 12 and somaH <= 24:
    somaH -= 12
elif somaH > 24:
    somaH -= 24
    if somaH > 12:
        somaH -=12

print(f"{somaH}:{somaMin:02d}")