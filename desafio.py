"""Dados os valores de horários, decifre a lógica e faça um código para executar:
entrada01: 3:45
entrada02: 14:20
saída: 6:05"""

""" Dividir horas e minutos para exibição
    *Converter na saída para formato 12h
    *Fazer um if para transformar 24h em 12h
"""

hora1 = int(input("Digite a primeira hora"))
#min1 =  int(input("Digite os minutos"))

hora2 = int(input("Digite a segunda hora"))
#min2 =  int(input("Digite os minutos"))

#Conversão das horas
if hora1 <= 12 and hora2 <= 12:
    somaH = hora1 + hora2
    #Print teste abaixo
    print(somaH)
else:
    if hora1 > 12 >= hora2:
        novaH = hora1-12
        hora1 = novaH
    elif hora2 > 12 >= hora1:
        novaH2 = hora2-12
        hora2 = novaH2
    else:
        novaH = hora1 - 12
        hora1 = novaH
        novaH2 = hora2 - 12
        hora2 = novaH2
    somaFinal = hora1 + hora2
    #Prints Testes abaixo:

    print(hora1)
    print(hora2)
    print(somaFinal)

#Conversão dos minutos
"""if min1 <=60 and min2 <=60:
    somaMin = min1 + min2
    print(somaMin)
else:
    if min1 >= 60 >= min2:
        novoMin1 = min1 - 60
        min1 = novoMin1
    elif min1 >= 60 >= min1:
        novoMin2 = min2 - 60
        min2 = novoMin2
    else:
        novoMin1 = min1 - 60
        min1 = novoMin1
        novoMin2 = min2 - 60
        min2 = novoMin2
    somaMin = min1 + min2
    print(min1)
    print(min2)
    print(somaMin)

"""





