Vai checar se o número é Par ou Ímpar
------------------------------------------------------------------------------------------
# Solicita ao usuário que digite um número inteiro 
numero = int(input("Digite o Número: "))

# Verifica se o número é divisível por 2 sem deixar resto
if numero % 2 == 0:
    # Se a condição for verdadeira, o número é par
    print(f"O número {numero} é par.")
else:
    # Se a condição for falsa, o número é ímpar
    print(f"O número {numero} é ímpar.")

