nascimento = int(input("Digite o ano de seu nascimento: "))
anoatual = int(input("Digite o ano atual: "))

idade = anoatual - nascimento

meses = idade * 12
dias = meses * 30

print(f"Idade: {idade} anos")
print(f"Idade em meses: {meses} meses")
print(f"Idade em dias (aprox): {dias} dias")