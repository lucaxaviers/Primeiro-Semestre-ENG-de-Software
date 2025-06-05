hrsTrabalhadas = float(input("Digite quantas horas foram trabalhadas: "))
sHora = float(input("Digite o valor pago por hora: "))

if hrsTrabalhadas > 40:
    salariobase = 40 * sHora
    horaextra = hrsTrabalhadas - 40
    salarioExtra = horaextra * (sHora * 1.5)
    salarioFinal = salariobase + salarioExtra
    print(f"O salario com horas extra é {salarioFinal}")

else:
    salarioFinal = hrsTrabalhadas * sHora
    print(f"O salario é {salarioFinal}")
    
