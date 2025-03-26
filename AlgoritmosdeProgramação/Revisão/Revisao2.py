# Criamos uma variável chamada "soma" e colocamos o valor 0 nela.
# Essa variável vai guardar a soma dos números.
soma = 0

# Criamos outra variável chamada "cont" e colocamos 0 nela.
# Essa variável vai contar quantos números estamos somando.
cont = 0

# Usamos um laço de repetição (for) para pegar os números de 15 até 100.
for X in range(15, 101):  # O range(15, 101) inclui os números de 15 a 100.
    # Adicionamos o valor de X à variável "soma".
    soma = soma + X

    # Aumentamos o contador em 1, pois adicionamos mais um número na soma.
    cont = cont + 1

# Agora, calculamos a média dividindo a soma total pela quantidade de números.
media = soma / cont

# Exibimos o resultado na tela.
print(f"A média é {media}")
