#   Escrever um algoritmo que leia uma quantidade desconhecida de Números e conte quantos deles estão nos seguintes intervalos: [0.25], [26,50], [51,75] e [76,100].
#   A entrada de dados deve terminar quando for lido um número negativo
cont1=0
cont2=0
cont3=0
cont4=0
n=0

n=int(input("Digite um N° e para parar digite um N° Negativo: "))

while (n >= 0 ):
    n=int(input("Digite um N° e para parar digite um N° Negativo: "))

    if (n<=25):
       cont1+=1

    elif (n<=50):
       cont2+=1
    
    elif (n<=75):
       cont3+=1
    
    else:
       cont4+=1

print(f"{cont1} [0,25]")
print(f"{cont2} [26,50]")
print(f"{cont3} [51,75]")
print(f"{cont4} [76,100]")