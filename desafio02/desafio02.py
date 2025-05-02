palavra = "vitor"
palavraCorreta = ["","","","",""]
count = 0

tentativa = " "

parada = 0

while count < 6 :
    erro = 0
    tentativa = input("Digite uma letra: ")
    for i in range(len(palavra)):
        if tentativa == palavra[i]:
            palavraCorreta[i] = palavra[i]
        else:
            erro +=1
    if erro == len(palavra):
        parada += 1

    count = parada

print(palavraCorreta)