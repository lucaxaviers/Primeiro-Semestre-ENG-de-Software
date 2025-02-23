Calcular o troco em Phyton apenas numeros inteiros
---------------------------------------------------
# Solicita os valores
recebido = int(input("Valor recebido: R$"))
compra = int(input("Valor da compra: R$"))

# Calcula o troco
troco = recebido - compra

# Verifica se o valor é suficiente
if troco < 0:
    print("Valor insuficiente. Não há troco.")
else:
    print(f"Troco a ser dado: R${troco}")
    
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    print("Troco em notas:")

    # Calcula o troco em notas
    for cedula in cedulas:
        qtd = troco // cedula
        troco %= cedula

        if qtd > 0:
            print(f"{qtd} nota(s) de {cedula}")
    
    # Caso sobrem centavos
    if troco > 0:
        print(f"Não foi possível entregar o troco completo. Sobrou {troco} centavos.")