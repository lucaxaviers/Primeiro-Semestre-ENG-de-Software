# Exibe a mensagem informando que serão mostrados os múltiplos de 7
print("Os números que são múltiplos de 7 são:")

# Laço 'for' para percorrer os números de 100 até 450 (inclusive)
for numero in range(100, 451):
    # Verifica se o número é múltiplo de 7 (resto da divisão por 7 é igual a 0)
    if numero % 7 == 0:
        # Se a condição for verdadeira, imprime o número
        print(numero)
