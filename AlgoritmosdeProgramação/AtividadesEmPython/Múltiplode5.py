# Solicita ao usuário para digitar um número e armazena na variável 'numero'
numero = float(input("Digite um numero: "))

# Verifica se o número é divisível por 5 (ou seja, se o resto da divisão por 5 é igual a 0)
if numero % 5 == 0:
    # Se a condição for verdadeira, exibe que o número é múltiplo de 5
    print("O número é múltiplo de 5")
else:
    # Se a condição não for verdadeira, exibe que o número não é múltiplo de 5
    print("Não é múltiplo de 5")
