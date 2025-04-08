# Solicita ao usuário que insira um número inteiro
num = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 3 e por 5 ao mesmo tempo
if num % 3 == 0 and num % 5 == 0:
    # Mostra que é divisível
    print(f"{num} é divisível por 3 e por 5 ao mesmo tempo")
else:
    # Caso não seja mostra que não é divisível
    print(f"{num} não é divisível por 3 e por 5 ao mesmo tempo")
