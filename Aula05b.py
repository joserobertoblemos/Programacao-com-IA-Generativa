#   Nesse Programa vamos estudar a estrutura de dados dicionário

aluno = {"Nome" : "Gaspar", "idade" : 17, "Nota" : 8.5}

print(f"Aluno: {aluno['Nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Nota: {aluno['Nota']}")

produto = {
    "Nome" : "Samsung Galaxy S20",
    "Categoria" : "Smartphone",
    "Marca" : "Samsung",
    "Preço" : 3500.00,
    "Quantidade" : 5,
    "Memória" : 8,
    "Capacidade" : 256
}

print("*" * 30)
# Imprimindo apenas as craves
for chave in produto:
    print(chave)
print("*" * 30)
# Imprimindo apenas os valores
for valor in produto.values():  #.values() ele vai pegar os valores ao invés do nome
    print(valor)

# Imprimindo chave e valor
for chave, valor in produto.items():    #.items() pega tudo, a chave e o valor do dicinário e colocar na esquerda e direita 
    print(f"{chave} : {valor}")
print("*" * 30)

