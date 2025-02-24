Calcula o salário bruto, o desconto de 8% e o salário líquido do encanador
----------------------------------------------------------------------------------

# Solicita a quantidade de dias trabalhados
dias = int(input("Digite a quantidade de Dias que o Encanador trabalhou= "))

# Calcula o salário bruto com base nos dias trabalhados (R$30 por dia)
bruto = dias * 30

# Calcula o desconto de 8% sobre o salário bruto
desconto = bruto * 0.08

# Calcula o salário líquido subtraindo o desconto do salário bruto
liquido = bruto - desconto

# Exibe o salário bruto
print(f"Salario Bruto: R$", bruto)

# Exibe o valor do desconto
print(f"Desconto: R$ ", desconto)

# Exibe o salário líquido após o desconto
print(f"Salario Liquido:R$ ", liquido)

