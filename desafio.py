"""Dados os valores de horários, decifre a lógica e faça um código para executar:
entrada01: 3:45
entrada02: 14:20
saída: 6:05"""

""" Dividir horas e minutos para exibição
    *Converter na saída para formato 12h
    *Fazer um if para transformar 24h em 12h
"""

hora1 = int(input("Digite a primeira hora"))
min1 =  int(input("Digite os minutos"))

hora2 = int(input("Digite a segunda hora"))
min2 =  int(input("Digite os minutos"))

if hora1 > 12:
    novaH = hora1-12
    hora1 = novaH
elif hora2 > 12:
    novaH2 = hora1 - 12
    hora2 = novaH2

somaH = hora1 + hora2

if somaH>12:
    horaFinal = somaH-12
    print(horaFinal)






"""elif min1>60:
    novoMin1 = min1/60"""





