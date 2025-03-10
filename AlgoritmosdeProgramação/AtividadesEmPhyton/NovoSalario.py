plano=int(input("Digite seu Plano de Trabalho sendo 1,2 ou 3: "))
salario=float(input("Digite seu Salario: "))

if plano==1:
   salario=salario* 1.1
   print(f"Seu novo salário é R${salario}");
   
if plano==2:
   salario=salario* 1.15
   print(f"Seu novo salário é R${salario}");
   
if plano==3:
   salario=salario* 1.20
   print(f"Seu novo salário é R${salario}");
