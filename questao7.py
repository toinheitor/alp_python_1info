idade = int(input("Digite sua idade: "))
habilitacao = input("Possui habilitação? (sim/não): ")

if idade >= 18 and habilitacao.lower() == "sim":
    print("Pode dirigir")

else:
    print("Não pode dirigir")
