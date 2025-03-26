mais50 = 0  # Contador de pessoas com mais de 50 anos
somaAltura = 0  # Soma das alturas para a média
contAltura = 0  # Contador de pessoas entre 10 e 20 anos
pesoMenor40 = 0  # Contador de pessoas com peso inferior a 40 kg

for i in range(25):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura (m): "))
    peso = float(input("Digite seu peso (kg): "))
    print("\n")

    # Conta pessoas com mais de 50 anos
    if idade > 50:
        mais50 += 1  

    # Soma altura das pessoas entre 10 e 20 anos
    if 10 <= idade <= 20:
        somaAltura = somaAltura+altura
        contAltura += 1  

    # Conta pessoas com peso inferior a 40 kg
    if peso < 40:
        pesoMenor40 += 1  

# Cálculo da média de altura
    mediaAltura = somaAltura / contAltura

# Cálculo da porcentagem de pessoas com peso inferior a 40 kg
percentualPesoMenor40 = (pesoMenor40 / 25) * 100  

# Exibe os resultados
print(f"{mais50} pessoas têm mais de 50 anos.")
print(f"A média das alturas das pessoas entre 10 e 20 anos é: {mediaAltura:.2f} m")
print(f"A porcentagem de pessoas com menos de 40 kg é: {percentualPesoMenor40:.2f}%")
