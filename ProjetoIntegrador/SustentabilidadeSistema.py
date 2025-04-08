# Inicializa contadores para os tipos de transporte
cont_transporte_sustentavel = 0
cont_transporte_nao_sustentavel = 0

# Coleta a data atual e os dados de consumo e geração de resíduos
data = input("Digite a data de hoje (DD/MM/AAAA): ")
consumo_agua = float(input("Digite o seu consumo diário de água (em litros): "))
consumo_energia = float(input("Digite o seu consumo diário de energia (em kWh): "))
geracao_residuos = int(input("Digite a porcentagem de geração de resíduos recicláveis: "))

# Calcula a porcentagem de resíduos não recicláveis
geracao_residuos_nao_reciclaveis = 100 - geracao_residuos

# Coleta as respostas sobre o uso de diferentes meios de transporte
print("\nResponda as pergunta a seguir com S/N com base no seu uso diário")
transporte_publico = input("Você usa transporte público? ") 
bicicleta = input("Você usa bicicleta no seu dia a dia? ")
caminhada = input("Você caminha até os lugares? ")
carro_fossil = input("Você usa carro a combustível fóssil? ")
carro_eletrico = input("Você usa carro elétrico? ")
carona = input("Você pega caronas (fossil)? ")

# Exibe a data informada
print(f"\nData de hoje: {data}")

# Avalia o consumo de água com base em faixas de sustentabilidade
if (consumo_agua < 150):
    print("Consumo de água: Alta Sustentabilidade")
elif (consumo_agua > 200):
    print("Consumo de água: Baixa Sustentabilidade")
else:
    print("Consumo de água: Moderada Sustentabilidade")

# Avalia o consumo de energia elétrica com base em faixas de sustentabilidade
if (consumo_energia < 5):
    print("Consumo de energia elétrica: Alta Sustetabilidade")
elif (consumo_energia > 10):
    print("Consumo de energia elétrica: Baixa Sustetabilidade")
else:
    print("Consumo de energia elétrica: Moderada Sustetabilidade")

# Avalia a quantidade de resíduos não recicláveis
if (geracao_residuos_nao_reciclaveis < 50):
    print("Geração de resíduos não recicláveis: Alta Sustetabilidade")
elif (geracao_residuos_nao_reciclaveis > 80):
    print("Geração de resíduos não recicláveis: Baixa Sustetabilidade")
else:
    print("Geração de resíduos não recicláveis: Moderada Sustetabilidade")

# Conta os meios de transporte sustentáveis utilizados
if (transporte_publico == "S"):
    cont_transporte_sustentavel += 1
if (carona == "S"):
    cont_transporte_nao_sustentavel += 1
if (bicicleta == "S"):
    cont_transporte_sustentavel += 1
if (caminhada == "S"):
    cont_transporte_sustentavel += 1
if (carro_eletrico == "S"):
    cont_transporte_sustentavel += 1
if (carro_fossil == "S"):
    cont_transporte_nao_sustentavel += 1

# Avalia o uso de transporte com base nos tipos utilizados
if (cont_transporte_sustentavel == 0):
    print("Uso de Transporte: Baixa Sustentabilidade") 
elif (cont_transporte_nao_sustentavel == 0):
    print("Uso de Transporte: Alta Sustentabilidade")
else:   
    print("Uso de Transporte: Moderada Sustentabilidade")
