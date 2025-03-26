# Criamos uma variável chamada "notasala" e colocamos o valor 0 nela.
# Essa variável vai armazenar a soma de todas as notas dos alunos.
notasala = 0

# Pede para o usuário digitar a quantidade de alunos na turma.
alunos = int(input("Digite a quantidade de alunos na turma: "))

# Usamos um laço (for) para repetir o processo de pedir as notas para cada aluno.
for i in range(alunos):  
    # Pede para o usuário digitar a nota de cada aluno e armazena o valor na variável "nota".
    nota = float(input(f"Digite a nota do aluno {i}:  "))  
    
    # Soma a nota de cada aluno à variável "notasala", que vai acumular todas as notas.
    notasala += nota  

# Calcula a média dividindo a soma das notas pelo número de alunos e exibe o resultado formatado com 2 casas decimais.
print(f"A média da sala foi {notasala/alunos:.2f}")
