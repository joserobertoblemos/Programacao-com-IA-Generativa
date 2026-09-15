# Crie um programa de aprendizado Supervisionado para treinar um modelo de acordo com as horas de estudo de um aluno
# Estudando 2, 3, 4 horas o aluno foi reprovado.
# Estudando 7, 8, 10 horas o aluno foi aprovado.


from sklearn.tree import DecisionTreeClassifier

# criar o x e o y e depois coloca o código para ele treinar e ai fornecer um hora como ex 7 horas

X = [
    [2],
    [3],
    [4],
    [7],
    [8],
    [10]
]

y = [0,0,0,1,1,1]

modelo = DecisionTreeClassifier()

modelo.fit(X, y)

novo_estudo = [[3]]

previsao = modelo.predict(novo_estudo)

if previsao [0] == 0 :  
    print("Reprovado")
else:
    print("Aprovado")
