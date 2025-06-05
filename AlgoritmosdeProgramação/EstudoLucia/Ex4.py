print("CALCULO SALARIO - INSS")
valorhora = float(input("Digite o valor da hora aula: "))
aulames = int(input("Digite quantas aulas por mês: "))
descontoINSS = float(input("Percentual descontado do INSS: "))

sbruto = valorhora * aulames
valorDesconto = (descontoINSS / 100) * sbruto
sliquido = sbruto - valorDesconto

print(f"Salário líquido: R$ {sliquido}")

