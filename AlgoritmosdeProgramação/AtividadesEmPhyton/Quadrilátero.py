# Solicita ao usuário para digitar a altura e armazena o valor em 'altura'
altura = float(input("Digite a altura: "))

# Solicita ao usuário para digitar a base e armazena o valor em 'base'
base = float(input("Digite a base: "))

# Verifica se a base e a altura são iguais
if base == altura:
    # Se a base for igual à altura, é um quadrado
    print("É um Quadrado")
else:
    # Se a base for diferente da altura, é um retângulo
    print("É um Retângulo")
