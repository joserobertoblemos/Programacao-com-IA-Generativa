# Uma imobiliária possui um arquivo chamado casas.csv contendo informações sobre imóveis.
# O arquivo possui as seguintes colunas:

# tamanho_m2
# preco_mil

# Utilize a biblioteca Pandas para realizar uma análise dos dados.

# Tarefas Crie um programa Python que:

# Importe a biblioteca Pandas.
# Leia o arquivo casas.csv.
# Armazene os dados em um DataFrame chamado casas.
# Exiba o DataFrame completo.
# Calcule e exiba a média do preço das casas.
# Exiba o menor preço encontrado.
# Exiba o maior preço encontrado.
# Conte quantas casas existem na base.
# Calcule a média do tamanho das casas.
# Exiba o menor e o maior tamanho das casas.

import pandas as pd

casas = pd.read_csv("casas.csv")

print(casas)

media_preco = int(casas["preco_mil"].mean())

menor_preco = casas["preco_mil"].min()

