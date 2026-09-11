# Nesse Programa vamos treinar o modelo de MachineLearning usando o Aprendizado Supervisionado
# nosso modelo deve analisar o assunto de um email e Classificar como SPAM ou NÂO SPAM

#Biblioteca que transforma textos em números
from sklearn.feature_extraction.text import CountVectorizer # vai transformar cada palavra em 0 e 1

#Biblioteca para criar o modelo com texto
from sklearn.naive_bayes import MultinomialNB

#Assuntos das Mensagens             #Quando vou treinar para saber quando é spam eu faço as mensagens que vai receber
mensagens = [
    "ganhe dinheiro agora",
    "clique e ganhe prêmio",
    "você ganhou um prêmio",
    "clique aqui e ganhe dinheiro",
    "reunião amanhã as 10 horas",
    "envie o relatório até sexta-feira",
    "segue relatório de vendas até agosto",
    "bom dia, professor"
]

#Definir ca categoria de cada mensagem
categorias = [
    "spam",
    "spam",
    "spam",
    "spam",
    "normal",
    "normal",
    "normal",
    "normal",
]

# Criar o conversor de texto para número
vetor = CountVectorizer()           # método do sciqtlear converte texto em número

# Aprende as palavras nas mensagens e transforma em números
X = vetor.fit_transform(mensagens)                  #algo parecido com Aula09a    

# Criar o modelo
modelo = MultinomialNB()

# Treinar o modelo
modelo.fit(X, categorias)


nova_mensagem = ["ganhe um prêmio hoje"]    #Essa nova msg precisa ser transformada em número

#Transformando em número

X_nova = vetor.transform(nova_mensagem)

# Previsão de SPAM ou NORMAL
resultado = modelo.predict(X_nova)

print(f"Mensagem: {nova_mensagem[0]}")
print(f"Resultado: {resultado[0]}")