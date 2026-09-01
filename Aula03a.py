# Nesse Progragama vamos fazer uma revisão dos pricipais comandos em python.

# Comando print()
print("Hello world!")
print('Olá mundo. Bem vindo ao python')
print('Não podemos "sujar" nossas mãos com o código sujo')

#Variáveis
aluno = "Gaspar" # tipo String (texto)
idade = 18       # tipo int (números inteiros)
altura = 1.70    # tipo float (numero de ponto flutuante ou decimal)
aluno_frequente = True  #tipo Boolean (verdadeiro ou falso)

# Imprimindo texto Literal com variáveis
print(f"Nome do aluno:   {aluno} tem {idade} anos e mede {altura} metros.")
 
# Operadores aritméticos
valor1 = 13
valor2 = 29
valor3 = 5.5
valor4 = 3.2

#Adição 
soma1 = valor1 + valor2
soma2 = valor3 + valor4
print(f"A soma de {valor1} e {valor2} é {soma1}")
print(f"A soma de {valor3} e {valor4} é {soma2}")
#Subtração 
sub1 = valor1 - valor2
sub2 = valor3 - valor4
print(f"A subtração de {valor1} por {valor2} é {sub1}")
print(f"A subtração de {valor3} por {valor4} é {sub2}")
#Multiplicação
mult1 = valor1 * valor2
mult2 = valor3 * valor4
print(f"A multiplicação de {valor1} por {valor2} é {mult1}.")
print(f"A multiplicação de {valor3} por {valor4} é {mult2}.")
#Divisão
div1 = valor1 / valor2
div2 = valor3 / valor4
print(f"A divisão de {valor1} por {valor2} é {div1:.4f}")
print(f"A divisão de {valor3} por {valor4} é {div2:.2f}")
# Divisão inteira
div3 = valor1 // valor2
div4 = valor3 // valor4
print(f"A divisão inteira de {valor1} por {valor2} é {div3}")
print(f"A divisão inteira de {valor3} por {valor4} é {div4}")
#resto da divisão (operador modulo -> %)
resto1 = valor2 % valor1
resto2 = valor3 % valor4
print(f"O resto da divisão de {valor2} por {valor1} é {resto1}")
print(f"O resto da divisão de {valor3} por {valor4} é {resto2}".replace(".",","))
#Potência
exp1 = valor1 ** 2
exp2 = valor2 ** 3
exp3 = valor3 ** 4
exp4 = valor4 ** 5
print(f"{valor1} elevado ao quadrado é {exp1}")
print(f"{valor2} elevado ao cubo é {exp2}")
print(f"{valor3} elevado a quarta Potência é {exp3:.2f}".replace(".",","))
print(f"{valor4} elevado a quinta Potência é {exp4:.2f}".replace(".",","))

# Operadores de atribuição composta
valor1 += 5 #equivalente a valor1 = valor1 + 5
valor2 -= 10 #equivalente a valor2 = valor2 - 10
valor3 *= 2 #equivalente a valor3 = valor3 * 2
valor4 /= 3 #equivalente a valor4 = valor4 / 4
print(f"Acrescentando 5 ao valor1 temos {valor1}")
print(f"Diminuindo 10 do valor2 temos {valor2}")
print(f"Multiplicando por 2 o valor3 temos {valor3}")
print(f"Dividindo por 3 o valor4 temos {valor4}")
