horas_trabalhadas_mes = int(input("Digite o número de horas trabalhadas no mês: "))
salario_por_hora = float(input("Digite o valor da sua hora de trabalho: "))

# Calculo do salário base
horas_normais = 40 * 4  
salario_base = salario_por_hora * horas_normais

# Verificando se houve horas extras
if horas_trabalhadas_mes > horas_normais:
    horas_extras = horas_trabalhadas_mes - horas_normais

    # Calculando o valor das horas extras (50% a mais do valor normal)
    valor_horas_extras = horas_extras * salario_por_hora * 1.5
    salario_total = salario_base + valor_horas_extras
    
else:
    salario_total = salario_base

# Exibindo o salário total
print(f"O salário total do funcionário é: R${salario_total:.2f}")
