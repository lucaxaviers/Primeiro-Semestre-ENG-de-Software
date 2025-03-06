Vê se o Numero é Positivo,Negativo ou nulo
--------------------------------------------------
#Pede o Numero
numero=float(input("Digite o Numero!  "))
#Vê se é Positivo
if numero>0:
   print(f"{numero:.0f} é Positivo")
#Vê se é Negativo
elif numero<0:
   print(f"{numero:.0f} é Negativo")
#Vê se é Nulo 
else:
    print(f"{numero:.0f} é Nulo")
