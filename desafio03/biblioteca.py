
def listar (lista):
    if lista:
        for i in range (1, len(lista)):
            print(f"Tarefa {i} - ", *lista[i])
    else:
        print("Lista vazia")

def inserir (lista):
    tarefa = input("Nova tarefa:")
    lista.append(tarefa)

def deletar (lista):
    numero = int(input("Digite o número da tarefa que deseja deletar: "))
    lista.remove(numero)