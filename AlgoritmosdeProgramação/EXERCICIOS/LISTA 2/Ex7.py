def somarDigitos(x):
    soma = 0
    for i in x:
        soma += int(i)
    return soma

def maiorDigito(x):
    maior = 0
    for i in x:
        if int(i) > maior:
            maior = int(i)
    return maior

numero = input("Digite um número: ")

x = somarDigitos(numero)
y = maiorDigito(numero)

print("Soma dos dígitos:", x)
print("Maior dígito:", y)
