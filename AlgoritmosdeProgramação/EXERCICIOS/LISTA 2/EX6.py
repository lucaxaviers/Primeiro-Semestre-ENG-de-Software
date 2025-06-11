def Fatorial(x):
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i
    return resultado

num = int(input("Digite um número: "))
chamar = Fatorial(num)
print(f"O fatorial de {chamar}")
