# Pede para o usuário digitar um número e guarda esse valor na variável A
A = int(input("Digite o Valor de A: "))

# Pede para o usuário digitar outro número e guarda esse valor na variável B
B = int(input("Digite o Valor de B: "))

# Pede para o usuário digitar mais um número e guarda esse valor na variável C
C = int(input("Digite o Valor de C: "))

# Soma os valores de A e B e guarda o resultado na variável "Soma"
Soma = A + B

# Agora, vamos comparar se a soma de A e B é maior que o número C
if Soma > C:
    # Se for maior, mostra uma mensagem dizendo que a soma passou de C
    print(f"A soma de A e B deu {Soma}, então é maior que C, que vale {C}")
else:
    # Se não for maior, mostra uma mensagem dizendo que a soma não passou de C
    print(f"A soma entre A e B é {Soma}, porém não é maior que C, pois C vale {C}")
