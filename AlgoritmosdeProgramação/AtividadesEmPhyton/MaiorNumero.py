Vai ver qual o maior entre três numeros inteiros
---------------------------------------------------------
# Solicita ao usuário que insira três números inteiros
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Variável maior pega o valor do primeiro número
maior = numero1

# Verifica se o segundo número é maior 
if numero2 > maior:
    maior = numero2

# Verifica se o terceiro número é maior que o atual "maior"
if numero3 > maior:
    maior = numero3

# Exibe o maior número
print(f"O maior número é: {maior}")
