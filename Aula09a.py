# Nesse Programa vamos estudar o aprendizado supervisionado de Machine Learning. Vamos simular um programa de classificação de spam
# scikit learning

from sklearn.tree import DecisionTreeClassifier # Para importar apenas essa sessão 

# Dados de treinamento 
# 1 = mensagens contendo palavras relacionadas a promoção/premio 
# 0 = Mensagem limpa, sem o conteúdo anterior.

X = [
    [1],    # "Você ganhou um premio"
    [1],    # "Clique aqui e ganhe dinheiro"
    [0],    # "Reunião amanhã as 10h"
    [0],    # "Segue o trabalho da aula"
    [1],    # "Parabéns você ganhou"
    [0]     # "Bom dia, professor"
]

# Respostas conhecidas
# 1 = Spam
# 2 = Não Spam
y = [1,1,0,0,1,0]

# Criando o modelo
modelo = DecisionTreeClassifier()

#Treinar o modelo utilizando os dados e as resposta
modelo.fit(X, y)

#Você não pode perder essa promoção
# 1 = possui caracteristica de spam
nova_mensagem = [[1]]

#Fazer a prescisao
previsao = modelo.predict(nova_mensagem)

#Mostra o resultado
if previsao [0] == 1:
    print("SPAM")
else:
    print("Não SPAM")



