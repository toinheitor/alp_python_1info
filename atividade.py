soma = 0
quantidade = 0
maior = 0

while True:
    numero = int(input("Digite um número inteiro positivo (negativo para encerrar): "))

    if numero < 0:
        break

    soma += numero
    quantidade += 1

    if quantidade == 1 or numero > maior:
        maior = numero

if quantidade > 0:
    media = soma / quantidade

    print("\nResultados:")
    print("a) Soma dos números:", soma)
    print("b) Média aritmética:", media)
    print("c) Maior número:", maior)
else:
    print("Nenhum número positivo foi informado.")
