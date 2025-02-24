##Converte o valor em dólares para reais com base na cotação informada
##----------------------------------------------------------------------------
# Exibe o título do cálculo
print("CONVERSÃO DE DÓLAR PARA REAIS")

# Solicita o valor em dólares
valor = float(input("Digite o valor em Dólar= "))

# Exibe a cotação padrão caso o usuário não saiba
print("Caso não saiba considere 5.726")

# Solicita a cotação do dólar
cotacao = float(input("Digite a Cotação do Dólar= "))

# Calcula e exibe o valor em reais com base na cotação fornecida
print(f"O valor em Reais é {valor * cotacao:.2f}")