def exibir_menu():
    print("\n--- To do list ---")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Consultar tarefa")
    print("4. Listar Todas as tarefas")
    print("5. Marcar tarefa como concluída")
    print("6. Sair")
    print("-------------------------")

# Passo 2: Função para adicionar um tarefa à lista
def adicionar_tarefa(lista):
    tarefa = input("Digite a tarefa: ")
    if tarefa in [t['nome'] for t in lista]:
        print(f"'{tarefa}' já existe na lista. Deseja atualizá-la? (s/n)")
        resposta = input().lower()
        if resposta != 's':
            print("Operação cancelada.")
            return # Sai da função se o usuário não quiser atualizar
    lista.append({"nome": tarefa, "concluida": False})
    print(f"Tarefa '{tarefa}' adicionada/atualizada com sucesso!")

# Passo 3: Função para remover um contato lista
def remover_tarefa(lista):
    tarefa = input("Digite o nome da tarefa que deseja remover: ")
    for t in lista:
        if t["nome"] == tarefa:
            lista.remove(t)
            print(f"Tarefa '{tarefa}' removida com sucesso!")
            return
    print(f"Tarefa '{tarefa}' não encontrada.")

# Passo 4: Função para consultar uma tarefa na lista
def consultar_tarefa(lista):
    tarefa = input("Digite o tarefa da tarefa que deseja consultar: ")
    for t in lista:
        if t["nome"] == tarefa:    
            status = "Concluída" if t["concluida"] else "Pendente"    
            print(f"Tarefa: {tarefa} | Status: {status}")
            return
    print(f"Tarefa '{tarefa}' não encontrada na lista.")


# Passo 5: Função para listar todos os contatos lista
def listar_tarefas(lista):
    if not lista:
        print("A lista está vazia.")
        return
    print("\n--- Tarefas na lista ---")
    for i, t in enumerate(lista):
        status = "✔️" if t["concluida"] else "❌"
        print(f"{i+1}. {t['nome']} [{status}]")
    print("-------------------------")

def marcar_como_concluida(lista):
    tarefa = input("Digite o nome da tarefa que deseja marcar como concluída: ")
    for t in lista:
        if t["nome"] == tarefa:
            t["concluida"] = True
            print(f"Tarefa '{tarefa}' marcada como concluída.")
            return
    print(f"Tarefa '{tarefa}' não encontrada.")

# Passo 6: Função principal que executalista telefônica
def main():
    # Loop principal do programa
    lista_de_tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ")

        if opcao == '1':
            adicionar_tarefa(lista_de_tarefas)
        elif opcao == '2':
            remover_tarefa(lista_de_tarefas)
        elif opcao == '3':
            consultar_tarefa(lista_de_tarefas)
        elif opcao == '4':
            listar_tarefas(lista_de_tarefas)
        elif opcao == '5':
            marcar_como_concluida(lista_de_tarefas)
        elif opcao == '6':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Escolha entre 1 e 6.")

# Passo 7: Executar a função principal quando o script é rodado
if __name__ == "__main__":
    main()