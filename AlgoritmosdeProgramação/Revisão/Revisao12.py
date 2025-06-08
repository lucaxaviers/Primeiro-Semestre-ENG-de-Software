n = int(input("Digite o valor de N: "))

if n == 1:
    termo = 1
elif n == 2:
    termo = 2
else:
    s1 = 1
    s2 = 2
    for i in range(3, n + 1):
        termo = 2 * s2 + s1
        s1, s2 = s2, termo

print(f"O {n}º termo da sequência é: {termo}")
------------------------------------------------------------------
n = int(input("Digite o valor de N: "))

if n == 0:
    soma = 0
elif n == 1:
    soma = 1
elif n == 2:
    soma = 1 + 2
else:
    s1 = 1
    s2 = 2
    soma = s1 + s2
    for i in range(3, n + 1):
        termo = 2 * s2 + s1
        soma += termo
        s1, s2 = s2, termo

print(f"A soma dos {n} primeiros termos da sequência é: {soma}")
