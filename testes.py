
hora1 = int(input("Digite a primeira hora"))
#min1 =  int(input("Digite os minutos"))

hora2 = int(input("Digite a segunda hora"))
#min2 =  int(input("Digite os minutos"))

somaH = hora1 + hora2

#Conversão das horas
if somaH >12:
    somaH -= 12
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

"""
somaMin = 0
#Conversão dos minutos
if min1 <=60 and min2 <=60:
    somaMin = min1 + min2
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
if somaMin > 60:
    somaMin -= 60
print(somaMin)"""