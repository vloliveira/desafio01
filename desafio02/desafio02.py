palavra = "abacate"
palavraCorreta = ["_"] * len(palavra)
tentativa = " "
count = 0
parada = 0
acertos = 0
mensagem = " "

desenho = [" ----------\n |        |\n |        \n |           \n |           \n_|__         \n",
           " ----------\n |        |\n |        O\n |           \n |           \n_|__         \n",
           " ----------\n |        |\n |        O\n |       /   \n |           \n_|__         \n",
           " ----------\n |        |\n |        O\n |       /|  \n |           \n_|__         \n",
           " ----------\n |        |\n |        O\n |       /|\\\n |           \n_|__         \n",
           " ----------\n |        |\n |        O\n |       /|\\\n |       /   \n_|__         \n",
           " ----------\n |        |\n |        O\n |       /|\\\n |       / \\\n_|__         \n"
           ]

print(desenho[0], *palavraCorreta)

while count < 6 :
    erro = 0

    tentativa = input("Digite uma letra: ")
    for i in range(len(palavra)):
        if tentativa == palavra[i]:
            palavraCorreta[i] = palavra[i]
            acertos += 1
        else:
            erro +=1
    if erro == len(palavra):
        parada += 1
        print(desenho[parada])
        print(*palavraCorreta)
        mensagem = "Você perdeu!"
    elif acertos == len(palavra):
        print(desenho[count])
        print(*palavraCorreta)
        mensagem = "Parabéns você acertou!"
        break
    else:
        print(desenho[count])
        print(*palavraCorreta)
    count = parada

print(mensagem)