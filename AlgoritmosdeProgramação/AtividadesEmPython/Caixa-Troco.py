Calcular o troco em Phyton apenas números inteiros (sem for e if)
-------------------------------------------------------------------
# Exibe o título do cálculo
print("CALCULO DO TROCO")

# Solicita os valores de dinheiro recebido e valor da compra
recebido = int(input("Valor recebido: R$"))
compra = int(input("Valor da compra: R$"))

# Calcula o troco
troco = recebido - compra

# Exibe o troco a ser dado
print(f"Troco a ser dado: R${troco}")

# Define as cédulas para o troco
cedulas = [100, 50, 20, 10, 5, 2, 1]
print("Troco em notas:")

# Calcula e exibe as cédulas no troco manualmente
qtd_100 = troco // 100
troco %= 100
qtd_50 = troco // 50
troco %= 50
qtd_20 = troco // 20
troco %= 20
qtd_10 = troco // 10
troco %= 10
qtd_5 = troco // 5
troco %= 5
qtd_2 = troco // 2
troco %= 2
qtd_1 = troco // 1

# Exibe diretamente as cédulas sem condições
print(f"{qtd_100} nota(s) de 100")
print(f"{qtd_50} nota(s) de 50")
print(f"{qtd_20} nota(s) de 20")
print(f"{qtd_10} nota(s) de 10")
print(f"{qtd_5} nota(s) de 5")
print(f"{qtd_2} nota(s) de 2")
print(f"{qtd_1} nota(s) de 1")