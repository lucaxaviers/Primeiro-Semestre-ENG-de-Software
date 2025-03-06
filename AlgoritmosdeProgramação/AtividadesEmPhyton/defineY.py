# Solicita que insira um número
x= float(input("Digite um número: "))

# Verifica se x é menor que 1
if x < 1:
    y = x  # Se x for menor que 1, y recebe o valor de x
    
# Verifica se x é igual a 1
elif x == 1:
    y = 0  # Se x = 1, y é igual a 0
    
# Se x for maior que 1
else:
    y = x ** 2  # Se x maior 1, y recebe o quadrado de x

# Exibe o valor calculado de y
print(f"O valor de y é: {y}")
