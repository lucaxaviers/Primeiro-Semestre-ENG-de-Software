# Pede para o usuário digitar três números e os armazena nas variáveis A, B e C
A = int(input("Digite um N°: "))
B = int(input("Digite um N°: "))
C = int(input("Digite um N°: "))

# Primeira Comparação: Verifica se A é o maior número
if A > B and A > C:
    # Se A for o maior, verificamos se B é maior que C
    if B > C:
        print(A, B, C)  # Se for, imprimimos A, B e C nessa ordem
    else:
        print(A, C, B)  # Caso contrário, imprimimos A, C e B

# Segunda Comparação: Verifica se B é o maior número
elif B > A and B > C:
    # Se B for o maior, verificamos se A é maior que C
    if A > C:
        print(B, A, C)  # Se for, imprimimos B, A e C nessa ordem
    else:
        print(B, C, A)  # Caso contrário, imprimimos B, C e A

# Terceira Comparação: Se nenhuma das anteriores foi verdadeira, C é o maior número
else:
    # Se C for o maior, verificamos se A é maior que B
    if A > B:
        print(C, A, B)  # Se for, imprimimos C, A e B nessa ordem
    else:
        print(C, B, A)  # Caso contrário, imprimimos C, B e A
