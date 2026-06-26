e1 = float(input("Digite a primeira estatura: "))
e2 = float(input("Digite a segunda estatura: "))
e3 = float(input("Digite a terceira estatura: "))

if e1 == e2 or e1 == e3 or e2 == e3:
    print("Há, pelo menos, 2 pessoas com a mesma estatura")

else:
    maior = e1

    if e2 > maior:
        maior = e2

    if e3 > maior:
        maior = e3

    print("Maior estatura:", maior)
