def somaImposto(taxaImposto, custo):
    taxaImposto = 1 + (taxaImposto/100)
    custo *= taxaImposto

    return custo

imposto = float(input("Digite o imposto do produto: "))
valor = float(input("Digite o valor de custo: "))

valorTotal = somaImposto(imposto, valor)

print(valorTotal)