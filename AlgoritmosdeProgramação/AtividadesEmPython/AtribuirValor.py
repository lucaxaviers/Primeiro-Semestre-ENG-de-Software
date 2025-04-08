# Solicita ao usuário para digitar o primeiro número e armazena na variável 'valor1'
valor1 = int(input("Digite um número: "))

# Solicita ao usuário para digitar o segundo número e armazena na variável 'valor2'
valor2 = int(input("Digite um número: "))

# Verifica se os dois números digitados são iguais
if valor1 == valor2:
    # Se os números forem iguais, realiza a soma dos dois números e armazena o resultado em 'valor'
    valor = valor1 + valor2
    # Exibe o resultado da soma
    print(f"A soma é {valor}")
else:
    # Se os números forem diferentes, realiza a multiplicação dos dois números e armazena o resultado em 'valor'
    valor = valor1 * valor2
    # Exibe o resultado da multiplicação
    print(f"A multiplicação é {valor}")
