
def listar (lista):
    if lista:
        for i in range (len(lista)):
            print(f"\nTarefa {i} - ", *lista[i], "\n")
    else:
        print("Lista vazia")

def inserir (lista):
    tarefa = input("Nova tarefa:")
    lista.append(tarefa)

def deletar (lista):
    print("\n")
    listar(lista)
    if lista:
        numero = int(input("Digite o número da tarefa que deseja deletar: "))
        if numero >=0 and numero <= len(lista):
            del lista[numero]
        else:
            print("Digite um número válido na lista!")