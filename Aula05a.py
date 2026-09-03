# Nesse Programa vamos estudar estruturas de dados.
# Vamos rever as listas e conhecer os dicionários do python

alunos = ["Gaspar", "Jorge", "Anabela", "Luiza"]
notas = [8.5, 4.5, 10.0, 6.5]

c = 0   #le-se contador

while c < len (alunos): #len() é uma contagem
    print(f"Aluno: {alunos[c]} - Nota: {notas[c]}")
    c += 1

print("*** Fim ***")

palavra = "GASPAR13"
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for letra in palavra:
    if letra.lower() in vogais:
        print(f"{letra} = Vogal")
    elif letra == " ":
        print(f"{letra} = Espaço")
    elif letra.isdigit():
        print(f"{letra} = Número")
    elif letra.lower() in consoantes:
        print(f"{letra} = Consoante")
    else:
        print(f"{letra} = Símbolo")
print("*** Fim ***")