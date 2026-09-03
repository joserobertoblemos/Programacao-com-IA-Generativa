# Sistema de Avaliação Escolar

# Você deve criar um programa em Python para calcular a média final de um estudante e informar sua situação acadêmica no final do bimestre. 
# Como o programa ainda não recebe dados digitados na hora, defina os valores diretamente nas variáveis.

# Requisitos:Crie variáveis para armazenar:
# O nome do aluno;
# Três notas (de 0 a 10).

# Calcule a média aritmética das três notas somando as notas e dividindo por 3.Use a estrutura de decisão (if, elif, else) para definir o status:
# Média maior ou igual a 7.0: "Aprovado"
# Média entre 5.0 e 6.9 (inclusive): "Recuperação"
# Média abaixo de 5.0: "Reprovado"
# Exiba na tela com print() o nome do aluno, a média calculada e a situação final.

nome_aluno = input("Digite o nome do Aluno: ")
print(f"Vamos Calcular a média do aluno {nome_aluno}")

nota1 =  1.5
nota2 =  1.4
nota3 =  3.8

media =  (nota1 + nota2 + nota3) / 3

situacao = ""

if media >= 7.0:
    situacao = "Aprovado"
elif media >= 5.0:
    situacao = "Recuperação"
elif media < 5.0 :
    situacao = "Reprovado"
else:
    situacao = "Nota inválida"

print(f"O Aluno {nome_aluno}, teve as notas {nota1}, {nota2} e {nota3} \n e obteve a média de {media:.2f} ")
print(f"Situação Final: {situacao}") 
