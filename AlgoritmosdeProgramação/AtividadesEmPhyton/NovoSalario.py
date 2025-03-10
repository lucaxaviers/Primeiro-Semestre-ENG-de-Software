# Solicita ao usuário para digitar o plano de trabalho (1, 2 ou 3)
plano = int(input("Digite seu Plano de Trabalho sendo 1, 2 ou 3: "))

# Solicita ao usuário para digitar seu salário
salario = float(input("Digite seu Salário: "))

# Verifica o plano de trabalho e calcula o novo salário baseado no plano escolhido
if plano == 1:
    # Se o plano for 1, o salário é aumentado em 10%
    salario = salario * 1.1
    print(f"Seu novo salário é R${salario:.2f}")
    
elif plano == 2:
    # Se o plano for 2, o salário é aumentado em 15%
    salario = salario * 1.15
    print(f"Seu novo salário é R${salario:.2f}")

elif plano == 3:
    # Se o plano for 3, o salário é aumentado em 20%
    salario = salario * 1.2
    print(f"Seu novo salário é R${salario:.2f}")

else:
    # Caso o plano inserido não seja 1, 2 ou 3, exibe uma mensagem de erro
    print("Plano inválido! Por favor, digite 1, 2 ou 3.")
