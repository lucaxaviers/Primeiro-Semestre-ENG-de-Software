# Pede para o usuário digitar o valor que ganha por hora-aula
HoraAula = float(input("Digite o valor da sua hora-aula: "))

# Pede para o usuário digitar quantas aulas deu no mês
Aulas = int(input("Digite quantas aulas foram dadas esse mês: "))

# Pede para o usuário digitar a porcentagem de desconto do INSS
desconto = float(input("Digite quantos %, o INSS desconta: "))

# Cálculo do salário bruto (antes do desconto)
salario = HoraAula * Aulas

# Cálculo do valor descontado pelo INSS
inss = salario * (desconto / 100)

# Cálculo do salário líquido (após o desconto)
salario = salario - inss

# Mostra os resultados para o usuário
print(f"\nFoi descontado do seu salário R${inss:.2f}")
print(f"Agora seu salário atualizado com o desconto é R${salario:.2f}")
