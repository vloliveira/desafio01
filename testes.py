
hora1 = int(input("Digite a primeira hora: "))
min1 =  int(input("Digite os minutos: "))

hora2 = int(input("Digite a segunda hora: "))
min2 =  int(input("Digite os minutos: "))

somaH = hora1 + hora2
somaMin = min1 + min2

#Conversão das horas
if somaH == 00:
    somaH = 12
elif somaH > 12 and somaH <= 24:
    somaH -= 12
else:
    somaH -= 24
    if somaH >12:
        somaH -=12

if somaMin == 00:
    somaMin = 60

if somaMin >= 60:
    somaH += 1
    somaMin -= 60


print(f"{somaH}:{somaMin:02d}")

