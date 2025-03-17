# Tabela de conversão de Fahrenheit para Celsius
print("Fahrenheit | Celsius")
print("--------------------")

# Converte Fahrenheit para Celsius de 30Fº a 51Fº
for fahrenheit in range(30, 51, 2):
    
# Calculo da conversão
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:^10} | {celsius:.2f}")
