#Escreva um que solicita 10 números ao usuário, e ao final mostre os dois maiores números digitados pelo usuário.
maior1=0
maior2=0
for cont in range(10):
    num=int(input("Digite um N°: "))
    
    if num > maior1:
        maior2 = maior1  # O maior2 recebe o valor do maior1
        maior1 = num      # O maior1 recebe o valor do número atual

    elif num > maior2:
        maior2 = num      # Caso o número seja maior que o Maior2

print(f"O maior número digitado foi: {maior1}")
print(f"O segundo maior número digitado foi: {maior2}")