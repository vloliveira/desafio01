palavra = "vitor"
palavraCorreta = []

tentativa = " "
erro = 0

while erro <= 6:
    tentativa = input("Digite uma letra: ")
    for i in range(len(palavra)):
        if tentativa == palavra[i]:
            palavraCorreta.insert(i, tentativa)
            break
        else:
            erro += 1

print(palavraCorreta)

#------------------------------------------------------------------------------

while count < 6:
    tentativa = input("Digite uma letra: ")
    for i in range(len(palavra)):
        if tentativa == palavra[i]:
            palavraCorreta[i] = palavra[i]
        else:
            erro +=1
    if erro == len(palavra):
       # mensagem = "Você perdeu"
        count += 1

#------------------------------------------------------------------------------



