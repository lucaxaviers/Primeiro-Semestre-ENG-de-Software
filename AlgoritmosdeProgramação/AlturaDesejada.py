Calcula quantos degraus são necessários para atingir a altura desejada
-------------------------------------------------------------------------
# Exibe o título do cálculo
print("CALCULO DE QUANTOS DEGRAUS VOCÊ VAI SUBIR")

# Solicita a altura de cada degrau
degrau = float(input("qual a altura do degrau da escada= "))

# Solicita a altura que o usuário deseja alcançar
altura = float(input("qual altura você quer chegar= "))

# Calcula e exibe a quantidade de degraus a serem subidos
print(f"Você vai subir {altura / degrau:.2f} degraus para chegar na altura desejada ")