# Nesse Programa vamos usar a biblioteca Pandas para completar dados faltantes

import pandas as pd

dados = {
    "nome": ["Gaspar", "Anabela", "Luiza", None, "Ana", "Carlos", "Camila"],
    "idade": [18, None, 25, 26, None, 18, 16],
    "notas": [7.0, 9.0, None, 6.5, 8.5, None, 9.0]
}

#Criando o DataFrame
alunos = pd.DataFrame(dados)

print(alunos)
print("*" * 30)

#Verificando quais dados estão faltando
print("Dados Faltantes")
print(alunos.isnull())  #.isnull vai falar quais itens estão faltando com True ou False
print("*" * 30)

#Contando quantos dados estão faltando em cada coluna
print("Quantidade de dados Faltantes")
print(alunos.isnull().sum())
print("*" * 30)

#Calculando a média das idades
media_idade = alunos["idade"].mean()
media_idade = int(media_idade)


#Calculando a média das notas
media_nota = alunos["notas"].mean()


#Preencher as idade faltantes com a média das idades
alunos["idade"] = alunos["idade"].fillna(media_idade)


#Preencher as notas faltantes com a média das notas
alunos["notas"] = alunos["notas"].fillna(media_nota)


#Preencher os nomes faltantes com a frase "não informado"
alunos["nome"] = alunos["nome"].fillna("Não informado")


#Mostrar a tabela depois de completar os dados
print(alunos)

#Criando um filtro dos alunos aprovados e reprovados
aprovados = alunos[alunos["notas"] >= 7]
reprovados = alunos[alunos["notas"] <= 7]

print("*" * 30)
print("Alunos Aprovados")
print(aprovados)
print("*" * 30)
print("Alunos Reprovados")
print(reprovados)