import random

print("🎮 ===>  BEM-VINDO AO JOGO SECRETO!  <=== 🎯")
print("------------------------------------------------")
print("👨‍💻 Desenvolvido por:")
print("Lucas Xavier, Mateus Oliveira,")
print("Wanderley Vieira e Arthur Grizone")
print("------------------------------------------------")
print("🎯 Objetivo: Descobrir um número secreto de 4 dígitos (entre 1000 e 9999) em até 10 tentativas!")
print("💡 A partir da 5ª tentativa, dicas mais completas serão reveladas!")
print("------------------------------------------------")

jogar_novamente = 1

while jogar_novamente == 1:
    code = random.randint(1000, 9999)
    digito1 = code // 1000
    digito2 = (code // 100) % 10
    digito3 = (code // 10) % 10
    digito4 = code % 10

    certo1 = -1
    certo2 = -1
    certo3 = -1
    certo4 = -1

    tentativa = 0
    acertou = 0

    for cont in range(10):
        if acertou == 0:
            tentativa = int(input(f"\n🧠 Tentativa {cont + 1}/10 - Digite um número entre 1000 e 9999: "))

            if 1000 <= tentativa <= 9999:
                if tentativa == code:
                    if cont == 0:
                        print("🎉 Parabéns! Você acertou o número SECRETO de primeira!!! 🥳")
                    else:
                        print(f"🎉 Parabéns! Você acertou o número na {cont + 1}ª tentativa! 🏆")
                    acertou = 1
                else:
                    tent1 = tentativa // 1000
                    tent2 = (tentativa // 100) % 10
                    tent3 = (tentativa // 10) % 10
                    tent4 = tentativa % 10

                    if tent1 == digito1:
                        certo1 = tent1
                    if tent2 == digito2:
                        certo2 = tent2
                    if tent3 == digito3:
                        certo3 = tent3
                    if tent4 == digito4:
                        certo4 = tent4

                    print(f"\n🔎 Dígitos corretos na posição: ", end="")

                    print(certo1 if certo1 != -1 else "_", end=" ")
                    print(certo2 if certo2 != -1 else "_", end=" ")
                    print(certo3 if certo3 != -1 else "_", end=" ")
                    print(certo4 if certo4 != -1 else "_")

                    print('\n')

                    quantidade_posicao_errada = 0
                    verificado_certo1 = -1
                    verificado_certo2 = -1
                    verificado_certo3 = -1
                    verificado_certo4 = -1
                    verificado_errado1 = -1
                    verificado_errado2 = -1
                    verificado_errado3 = -1
                    verificado_errado4 = -1

                    if tent1 != digito1 and verificado_certo1 == -1:
                        if tent1 == digito2 and verificado_certo2 == -1 and verificado_errado2 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado1 = 1
                            verificado_errado2 = 1
                        elif tent1 == digito3 and verificado_certo3 == -1 and verificado_errado3 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado1 = 1
                            verificado_errado3 = 1
                        elif tent1 == digito4 and verificado_certo4 == -1 and verificado_errado4 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado1 = 1
                            verificado_errado4 = 1

                    if tent2 != digito2 and verificado_certo2 == -1:
                        if tent2 == digito1 and verificado_certo1 == -1 and verificado_errado1 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado2 = 1
                            verificado_errado1 = 1
                        elif tent2 == digito3 and verificado_certo3 == -1 and verificado_errado3 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado2 = 1
                            verificado_errado3 = 1
                        elif tent2 == digito4 and verificado_certo4 == -1 and verificado_errado4 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado2 = 1
                            verificado_errado4 = 1

                    if tent3 != digito3 and verificado_certo3 == -1:
                        if tent3 == digito1 and verificado_certo1 == -1 and verificado_errado1 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado3 = 1
                            verificado_errado1 = 1
                        elif tent3 == digito2 and verificado_certo2 == -1 and verificado_errado2 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado3 = 1
                            verificado_errado2 = 1
                        elif tent3 == digito4 and verificado_certo4 == -1 and verificado_errado4 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado3 = 1
                            verificado_errado4 = 1

                    if tent4 != digito4 and verificado_certo4 == -1:
                        if tent4 == digito1 and verificado_certo1 == -1 and verificado_errado1 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado4 = 1
                            verificado_errado1 = 1
                        elif tent4 == digito2 and verificado_certo2 == -1 and verificado_errado2 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado4 = 1
                            verificado_errado2 = 1
                        elif tent4 == digito3 and verificado_certo3 == -1 and verificado_errado3 == -1:
                            quantidade_posicao_errada += 1
                            verificado_errado4 = 1
                            verificado_errado3 = 1

                    if quantidade_posicao_errada > 0:
                        if quantidade_posicao_errada == 1:
                            print("⚠️ Você acertou 1 dígito, mas está na posição errada.")
                        else:
                            print(f"⚠️ Você acertou {quantidade_posicao_errada} dígitos, mas estão nas posições erradas.")

                    if cont >= 4:
                        print("\n🔍 Dicas:")
                        if certo1 == -1:
                            print(f"👉 O 1º dígito é {'MAIOR' if digito1 > 5 else 'MENOR ou IGUAL'} a 5.")
                        if certo2 == -1:
                            print(f"👉 O 2º dígito é {'MAIOR' if digito2 > 5 else 'MENOR ou IGUAL'} a 5.")
                        if certo3 == -1:
                            print(f"👉 O 3º dígito é {'MAIOR' if digito3 > 5 else 'MENOR ou IGUAL'} a 5.")
                        if certo4 == -1:
                            print(f"👉 O 4º dígito é {'MAIOR' if digito4 > 5 else 'MENOR ou IGUAL'} a 5.")

                    if cont >= 5:
                        if certo1 == -1:
                            print(f"🔢 O 1º dígito é {'PAR' if digito1 % 2 == 0 else 'ÍMPAR'}.")
                        if certo2 == -1:
                            print(f"🔢 O 2º dígito é {'PAR' if digito2 % 2 == 0 else 'ÍMPAR'}.")
                        if certo3 == -1:
                            print(f"🔢 O 3º dígito é {'PAR' if digito3 % 2 == 0 else 'ÍMPAR'}.")
                        if certo4 == -1:
                            print(f"🔢 O 4º dígito é {'PAR' if digito4 % 2 == 0 else 'ÍMPAR'}.")
                    print("--------------------------------------------------")
            else:
                print("🚫 Número fora do intervalo! Digite um número entre 1000 e 9999.")

    if acertou == 0:
        print(f"\n😢 Que pena! Você não acertou. O número secreto era {code}. ❌")

    print("\n🙏 Obrigado por jogar o Jogo Secreto!")

    print("\n🔁 Deseja jogar novamente?")
    print("1️  - Sim")
    print("2️  - Não")
    jogar_novamente = int(input("📝 Digite sua escolha: "))
    print("--------------------------------------------------")
    if jogar_novamente == 1: 
        if acertou == 1:
            print("👑 Bem vindo de volta Campeão!")
        if acertou == 0:
            print("💪 Você não desiste fácil, hein!")
            print("➡️ Vamos para a próxima então!")
    else:
        print("🙌 Obrigado por jogar o Jogo Secreto! Até a próxima! 👋")
