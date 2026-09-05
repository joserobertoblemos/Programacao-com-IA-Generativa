# Nesse Programa vamos estudar a biblioteca Pandas, essa bibiliteca cria um DataFrame (tabela) 
# a partir de um array, arquivo csv, planilha do Excel, etc.

import pandas as pd

# Utilizando um dicinário contendo informações dos alunos
# Cada 'chave' desse dicinário contém uma lista no 'valor'
# Cada 'chave' representa uma coluna da tabela 

dados = {
    "nome": ["Gaspar", "Anabela", "Luiza", "Jorge", "Ana", "Carlos", "Camila"],
    "idade": [18, 16, 25, 26, 17, 18, 16],
    "nota": [7.0, 9.0, 8.5, 6.5, 8.5, 7.0, 9.0]
}

print("Dicionário com dados dos alunos") 
print(dados)

#Criar um DataFrame a partir do dicionário
alunos = pd.DataFrame(dados)

print("*" * 30)
print(alunos)
print("*" * 30)

#Imprimindo a coluna nome
print(alunos["nome"])
print("*" * 30)

#Imprimindo a coluna nota
print(alunos["nota"])
print("*" * 30)

#Imprimindo uma linha inteira
print(alunos.iloc[1])
print("*" * 30)

#Imprimindo apenas um item da tabela
print(alunos["nome"].iloc[3])
print("Idade", alunos["idade"].iloc[3])
print("nota", alunos["nota"].iloc[3])

#Criando uma estrutura de dados de uma coluna
notas = alunos["nota"]
print("*" * 30)
print(notas)
print("*" * 30)

print("Média das notas: ", notas.mean())
print("Maior nota: ", notas.max())
print("Menor nota: ", notas.min())
print("Quantidade de notas: ", notas.count())
print("*" * 30)