import os


def limpar_tela():
    # Limpa a tela no Windows, Linux e macOS
    os.system("cls" if os.name == "nt" else "clear")


while True:
    # =========================
    # TELA DE LOGIN
    # =========================
    limpar_tela()

    print("=" * 40)
    print("       SISTEMA DE GERENCIAMENTO")
    print("                 LOGIN")
    print("=" * 40)

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "123":
        print("\nLogin realizado com sucesso!")
        input("Pressione ENTER para continuar...")

        # =========================
        # MENU PRINCIPAL
        # =========================
        while True:
            limpar_tela()

            print("=" * 40)
            print("       SISTEMA DE GERENCIAMENTO")
            print("              MENU PRINCIPAL")
            print("=" * 40)
            print("1 - Cadastrar usuário")
            print("2 - Listar usuários")
            print("3 - Alterar usuário")
            print("4 - Excluir usuário")
            print("5 - Logout")
            print("6 - Encerrar")
            print("=" * 40)

            opcao = input("Escolha uma opção: ")

            if opcao == "5":
                # Volta para a tela de login
                print("\nSaindo da conta...")
                input("Pressione ENTER para voltar ao login...")
                break

            elif opcao == "6":
                # Encerra completamente o programa
                limpar_tela()
                print("Programa encerrado.")
                exit()

            else:
                # As demais opções ainda não funcionam
                print("\nEsta opção ainda não está disponível.")
                input("Pressione ENTER para voltar ao menu...")

    else:
        print("\nUsuário ou senha incorretos!")
        input("Pressione ENTER para tentar novamente...")
