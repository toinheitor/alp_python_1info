salario = float(input("Digite o salário: "))
cargo = input("Digite o cargo: ")

if cargo == "Programador de Sistemas":
    novo_salario = salario * 1.30
    print("Novo salário:", novo_salario)

elif cargo == "Analista de Sistemas":
    novo_salario = salario * 1.20
    print("Novo salário:", novo_salario)

elif cargo == "Analista de Banco de Dados":
    novo_salario = salario * 1.15
    print("Novo salário:", novo_salario)

else:
    print("Cargo inválida")
