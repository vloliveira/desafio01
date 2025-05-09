# Lista de tarefas

from biblioteca import listar, inserir, deletar

lista = []

while True:
    print("\nMenu: \n")
    print("Digite 1 para listar todas as tarefas")
    print("Digite 2 para inserir uma nova tarefa")
    print("Digite 3 para deletar uma tarefa")
    print("Digite 0 para sair.\n")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            listar(lista)
        case 2:
            inserir(lista)
        case 3:
            deletar(lista)
        case 0:
            break
        case _:
            print("Opção inválida, tente novamente!")
