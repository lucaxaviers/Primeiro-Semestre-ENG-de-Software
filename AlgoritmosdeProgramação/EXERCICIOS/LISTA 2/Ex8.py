def numeroPerfeito():
        soma = 0
        x = int(input("Digite um numero: "))

        for i in range (1,x):
                
             if x % i == 0:
                soma += i

        if soma == x:
             print("PERFEITO")
        else:
             print("NAO PERFEITO")
            

numeroPerfeito() 