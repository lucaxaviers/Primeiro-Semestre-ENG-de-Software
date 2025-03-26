# Inicializa as variáveis
total_salarios = 0
total_filhos = 0
maior_salario = 0
salarios_menor_1500 = 0
habitantes = 0

# Coleta de dados até que o usuário digite um salário negativo
salario = float(input("Digite o salário (ou um valor negativo para sair): "))

while salario >= 0:
    filhos = int(input("Digite o número de filhos: "))

    total_salarios += salario
    total_filhos += filhos
    habitantes += 1

    if salario > maior_salario:
        maior_salario = salario

    if salario < 1500:
        salarios_menor_1500 += 1

    salario = float(input("Digite o salário (ou um valor negativo para sair): "))

# Exibe os resultados
print(f"\nMédia de salário: R${total_salarios / habitantes:.2f}")
print(f"Média de filhos: {total_filhos / habitantes:.2f}")
print(f"Maior salário: R${maior_salario:.2f}")
print(f"Percentual com salário < R$1500: {(salarios_menor_1500 / habitantes) * 100:.2f}%")
