voos = {}
passageiros = {}
dados_passageiros = {}

def cadastrar_voo():
    codigovoo = input("Digite o código do voo: ").lower()
    if codigovoo in voos:
        print("Erro: esse código de voo já foi cadastrado.")
    else:
        origem = input("Digite a cidade de origem: ").lower()
        destino = input("Digite a cidade de destino: ").lower()
        escalas = int(input("Digite o número de escalas: "))
        preco = float(input("Digite o preço da passagem: "))
        lugaresdisp = int(input("Digite o número de lugares disponíveis: "))

        voos[codigovoo] = {"origem": origem,"destino": destino,"escalas": escalas,"preco": preco,"lugares_disponiveis": lugaresdisp}
        print(f"Voo {codigovoo} cadastrado com sucesso!")

def consultar_voos():
    print("1 - Pelo código do voo")
    print("2 - Por cidade de origem")
    print("3 - Por cidade de destino")
    print("4 - Voltar ao menu principal")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        codigovoo = input("Digite o código do voo: ").lower()
        if codigovoo in voos:
            voo = voos[codigovoo]
            print(f"\nInformações do Voo {codigovoo}:")
            print(f"Origem: {voo['origem']}")
            print(f"Destino: {voo['destino']}")
            print(f"Escalas: {voo['escalas']}")
            print(f"Preço: R${voo['preco']:.2f}")
            print(f"Lugares disponíveis: {voo['lugares_disponiveis']}")
        else:
            print("Erro: voo não encontrado.")

    elif opcao == 2:
        origem = input("Digite a cidade de origem: ").lower()
        for codigo, voo in voos.items():
            if voo['origem'] == origem:
                print(f"Código: {codigo} | Destino: {voo['destino']} | Preço: R${voo['preco']:.2f}")

    elif opcao == 3:
        destino = input("Digite a cidade de destino: ").lower()
        for codigo, voo in voos.items():
            if voo['destino'] == destino:
                print(f"Código: {codigo} | Origem: {voo['origem']} | Preço: R${voo['preco']:.2f}")

def voo_com_menos_escalas():
    origem = input("Digite a cidade de origem: ").lower()
    destino = input("Digite a cidade de destino: ").lower()
    menor_escalas = float('inf')
    melhor_codigo = ""

    for codigo, voo in voos.items():
        if voo["origem"] == origem and voo["destino"] == destino:
            if voo["escalas"] < menor_escalas:
                menor_escalas = voo["escalas"]
                melhor_codigo = codigo

    if melhor_codigo:
        voo = voos[melhor_codigo]
        print(f"\nVoo com menos escalas: {melhor_codigo}")
        print(f"Escalas: {voo['escalas']}")
        print(f"Preço: R${voo['preco']:.2f}")
    else:
        print("Nenhum voo encontrado com essa origem e destino.")

def listar_passageiros():
    codigovoo = input("Digite o código do voo para listar passageiros: ").lower()
    if codigovoo not in voos:
        print("Voo não encontrado.")
    else:
        passageiros_do_voo = [cpf for cpf, voos_p in passageiros.items() if codigovoo in voos_p]
        if not passageiros_do_voo:
            print("Nenhum passageiro cadastrado para este voo.")
        else:
            print(f"Passageiros do voo {codigovoo}:")
            for cpf in passageiros_do_voo:
                nome = dados_passageiros[cpf]["nome"]
                telefone = dados_passageiros[cpf]["telefone"]
                print(f"CPF: {cpf}, Nome: {nome}, Telefone: {telefone}")

def vender_passagem():
    nome = input("Digite o nome do passageiro: ")
    cpf = input("Digite o CPF do passageiro: ")
    telefone = input("Digite o telefone do passageiro: ")
    codigovoo = input("Digite o código do voo: ").lower()

    if codigovoo not in voos:
        print("Código de voo inválido.")
    elif voos[codigovoo]['lugares_disponiveis'] <= 0:
        print("Não há lugares disponíveis nesse voo.")
    else:
        dados_passageiros[cpf] = {"nome": nome, "telefone": telefone}

        voos[codigovoo]['lugares_disponiveis'] -= 1

        if cpf not in passageiros:
            passageiros[cpf] = []

        if codigovoo not in passageiros[cpf]:
            passageiros[cpf].append(codigovoo)

        print("Passagem vendida com sucesso!")

def cancelar_passagem():
    cpf = input("Digite o CPF do passageiro para cancelar passagem: ")
    codigovoo = input("Digite o código do voo: ").lower()

    if cpf in passageiros and codigovoo in passageiros[cpf]:
        passageiros[cpf].remove(codigovoo)
        voos[codigovoo]['lugares_disponiveis'] += 1
        print(f"Passagem cancelada com sucesso!")
    else:
        print("Passagem não encontrada para o CPF e voo informados.")

opcaomenu = 0
while opcaomenu != 7:
    print(f"\nSeja Bem-Vindo ao Sistema de Passagem Aérea\n")
    print("1 - Cadastrar Voo")
    print("2 - Consultar Voos")
    print("3 - Voo com menos escalas")
    print("4 - Listar Passageiros de um Voo")
    print("5 - Vender Passagem")
    print("6 - Cancelar Passagem")
    print("7 - Sair\n")

    opcaomenu = int(input("Digite a opção desejada: "))

    if opcaomenu == 1:
        cadastrar_voo()
    elif opcaomenu == 2:
        consultar_voos()
    elif opcaomenu == 3:
        voo_com_menos_escalas()
    elif opcaomenu == 4:
        listar_passageiros()
    elif opcaomenu == 5:
        vender_passagem()
    elif opcaomenu == 6:
        cancelar_passagem()
    elif opcaomenu == 7:
        print("Saindo do sistema. Até logo!")
    else:
        print("Opção inválida. Tente novamente.")
