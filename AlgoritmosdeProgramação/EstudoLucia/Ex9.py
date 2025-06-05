# numero = 0
# soma = 0

# for i in range (1,11):
#     numero = int(input(f"Digite o {i}° numero: "))
#     soma = numero + soma
#     media = soma/i 
# print(f"A média dos numeros digitados é {media}")

numero = 0
for i in range (1,11):
    numero += int(input(f"Digite o {i}° numero: "))
print(f"A média dos numeros digitados é {numero/i}")
