# Elabore um programa que leia um número e imprima todos os números divisíveis por 4 que sejam menores que este número lido

# pede um número pro usuário
numero = int(input("Digite um número: "))

# Mostra os números divisíveis por 4 e menores que o número informado
print(f"Números divisíveis por 4 menores que {numero}:")

# Percorre os números de 1 até o número informado (sem contar ele)
for i in range(numero):
    # Verifica se o número é divisível por 4
    if i % 4 == 0:
        print(i)

