n1 = int(input("Digite o valor de A: "))
n2 = int(input("Digite o valor de B: "))
n3 = int(input("Digite o valor de C: "))


if n1 > n2 and n2 > n3:
    print(n1, n2, n3)
elif n1 > n3 and n3 > n2:
    print(n1, n3, n2)
elif n2 > n1 and n1 > n3:
    print(n2, n1, n3)
elif n2 > n3 and n3 > n1:
    print(n2, n3, n1)
elif n3 > n1 and n1 > n2:
    print(n3, n1, n2)
else:
    print(n3, n2, n1)
