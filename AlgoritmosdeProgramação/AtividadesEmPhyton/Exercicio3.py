#Escreva um que solicita 10 números ao usuário, e ao final mostre os dois maiores números digitados pelo usuário.
maior1=0

#Vai pedir 10 N°s para o usuario
for cont in range(10):
    num=int(input("Digite um N°: "))
    
#Confere o maior
    if num > maior1:
        maior2 = maior1  # O maior2 recebe o valor do maior1
        maior1 = num      # O maior1 recebe o valor do número atual

    elif num > maior2:
        maior2 = num      # Caso o não seja maior que o número maior1, porem maior que o Maior2

#Mostra o maior e o segundo maior
print(f"O maior número digitado foi: {maior1}")
print(f"O segundo maior número digitado foi: {maior2}")