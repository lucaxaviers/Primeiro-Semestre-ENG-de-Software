# Criação de uma lista para armazenar os dados dos alunos
alunos = []

# Solicita ao usuário a quantidade de alunos a serem cadastrados
qntdaluno = int(input("Quantos alunos serão cadastrados? "))

# Loop para cadastrar cada aluno
for i in range(qntdaluno):
    # Exibe o número do aluno sendo cadastrado
    print(f"\nAluno {i+1}:")
    
    # Solicita os dados do aluno: nome e notas das provas e dos projetos
    nome = input("Nome: ")
    T1 = float(input("T1: "))  # Nota da primeira prova teórica
    T2 = float(input("T2: "))  # Nota da segunda prova teórica
    P1 = float(input("P1: "))  # Nota do primeiro projeto
    P2 = float(input("P2: "))  # Nota do segundo projeto
    
    # Calcula a média teórica (MT) e a média prática (MP)
    MT = 0.4 * T1 + 0.6 * T2  # Média teórica com peso 0.4 para T1 e 0.6 para T2
    MP = (P1 + P2) / 2  # Média prática é a média simples entre P1 e P2

    # Calcula a média final (MF) de acordo com as regras fornecidas
    if MT > 5.0 and MP > 5.0:
        MF = 0.3 * MP + 0.7 * MT  # Média final com peso 0.3 para MP e 0.7 para MT, se ambas forem > 5
    else:
        # Se alguma média for menor ou igual a 5, a MF é a menor entre MT e MP
        if MT < MP:
            MF = MT
        else:
            MF = MP

    # Armazena as informações do aluno na lista 'alunos'
    alunos.append([nome, [T1, T2], [P1, P2], [MT, MP], MF])

# Exibe o menu de opções
print(f"\nMENU DE OPÇÕES\n 1-Boletim da Sala\n 2-Buscar pelo Nome\n 3-Maior Nota\n 4-Menor Nota\n 5-Aprovados\n 6-Sair")
# Solicita que o usuário escolha uma opção do menu
opcao = input("Opção: ")

# Loop que mantém o programa em execução até que o usuário escolha a opção 6 (Sair)
while opcao != "6":
    
    # Opção 1: Imprimir boletim com as médias dos alunos
    if opcao == "1":
        print("\nNome            MT  MP  MF")
        # Imprime as informações de cada aluno no formato especificado
        for aluno in alunos:
            print(f"{aluno[0]:<15}{aluno[3][0]:<4.1f}{aluno[3][1]:<4.1f}{aluno[4]:<4.1f}")

    # Opção 2: Buscar informações de um aluno pelo nome
    elif opcao == "2":
        nome_busca = input("Nome: ")
        encontrado = False
        # Loop para encontrar o aluno
        for aluno in alunos:
            if aluno[0] == nome_busca:
                # Exibe todas as informações do aluno encontrado
                print(f"\nNome: {aluno[0]}\nT1: {aluno[1][0]} T2: {aluno[1][1]}\nP1: {aluno[2][0]} P2: {aluno[2][1]}")
                print(f"MT: {aluno[3][0]:.1f} MP: {aluno[3][1]:.1f} MF: {aluno[4]:.1f}")
                encontrado = True
        if not encontrado:
            print("Aluno não encontrado!")

    # Opção 3: Mostrar o nome do aluno com a maior média final
    elif opcao == "3":
        if alunos:
            maiornota = alunos[0]  # Assume que o primeiro aluno tem a maior média
            for aluno in alunos:
                if aluno[4] > maiornota[4]:
                    maiornota = aluno  # Atualiza a maior média se encontrado um aluno com média maior
            print(f"\nMaior Média Final: {maiornota[0]} com {maiornota[4]:.1f}")
        else:
            print("Nenhum aluno cadastrado!")

    # Opção 4: Mostrar o nome do aluno com a menor média final
    elif opcao == "4":
        if alunos:
            menornota = alunos[0]  # Assume que o primeiro aluno tem a menor média
            for aluno in alunos:
                if aluno[4] < menornota[4]:
                    menornota = aluno  # Atualiza a menor média se encontrado um aluno com média menor
            print(f"\nMenor Média Final: {menornota[0]} com {menornota[4]:.1f}")
        else:
            print("Nenhum aluno cadastrado!")

    # Opção 5: Calcular e mostrar o percentual de alunos aprovados
    elif opcao == "5":
        aprovados = 0
        # Conta o número de alunos com média final superior a 5
        for aluno in alunos:
            if aluno[4] > 5:
                aprovados += 1
        # Calcula o percentual de alunos aprovados
        percaprovados = (aprovados / qntdaluno) * 100
        print(f"\nAlunos Aprovados: {percaprovados:.1f}%")

    # Caso a opção fornecida não seja válida
    else:
        print("Opção inválida!")

    # Exibe novamente o menu de opções
    print(f"\nMENU DE OPÇÕES\n 1-Boletim da Sala\n 2-Buscar pelo Nome\n 3-Maior Nota\n 4-Menor Nota\n 5-Aprovados\n 6-Sair")
    # Solicita que o usuário escolha uma nova opção
    opcao = input("Opção: ")

# Quando o usuário escolhe a opção 6, o programa é encerrado
print("\nPrograma encerrado.")
