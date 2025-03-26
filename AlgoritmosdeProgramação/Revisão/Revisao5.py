# Pede para o usuário digitar o ano em que nasceu
data = int(input("Digite o ano que você nasceu: "))

# Calcula a idade subtraindo o ano de nascimento do ano atual (2025)
anos = 2025 - data

# Calcula a idade em meses (considerando 12 meses por ano)
meses = anos * 12

# Calcula a idade aproximada em dias (considerando 365 dias por ano)
dias = anos * 365

# Exibe o resultado na tela
print(f"Você tem {anos} anos, {meses} meses e aproximadamente {dias} dias.")
