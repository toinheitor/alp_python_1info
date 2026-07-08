tentativas = 0

while tentativas < 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == "aluno" and senha == "12345":
        print("Acesso liberado")
        break
    else:
        tentativas += 1

        if tentativas == 3:
            print("Você tentou 3 vezes")
        else:
            print("Tente novamente")
