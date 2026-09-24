import random

while True:
    print("\n=== JOGO DE ADIVINHAÇÃO ===")
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil   (1 a 10)")
    print("2 - Médio   (1 a 20)")
    print("3 - Difícil (1 a 30)")

    dificuldade = int(input("Digite o nível escolhido: "))

    if dificuldade == 1:
        limite = 10
    elif dificuldade == 2:
        limite = 20
    elif dificuldade == 3:
        limite = 30
    else:
        print("Opção inválida! Escolha uma dificuldade válida.")
        continue

    numero_sorteado = random.randint(1, limite)
    acertou = False

    print(f"\nTente adivinhar o número entre 1 e {limite}!")
    print("Você tem até 3 chances.")

    for tentativa in range(1, 4):
        numero = int(input(f"\nTentativa {tentativa}: Digite seu palpite: "))

        if numero == numero_sorteado:
            print("Parabéns, você acertou!")
            acertou = True
            break

        print("Você errou!")

        if numero < numero_sorteado:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

    if not acertou:
        print("\nVocê perdeu! Fim de jogo.")
        print(f"O número sorteado era {numero_sorteado}.")

    jogar_novamente = input("\nVocê quer jogar novamente? (s/n): ").lower()

    if jogar_novamente != "s":
        print("Obrigado por jogar! Até a próxima!")
        break

