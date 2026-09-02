#Nesse programa vamos estudar a estrutura de repetição while

contador = 1

while contador <= 10:
    print(f"Número {contador}")
    contador += 1   #equivalente a contador = contador + 1

print("=" * 40)
print("Fim da sequencia")
print("=" * 40)

contador = 2

# imprimindo os pares de 2 a 20
while contador <= 20:
    print(contador, end = " - ")
    contador += 2

print()
print("=" * 40)
print("Fim da sequencia")
print("=" * 40)

# imprimindo a potencia de 5 até 5000
contador = 5

while contador <= 5000:
    print(contador, end = ", ")
    contador *= 5


print()
print("=" * 40)
print("Fim da sequencia")
print("=" * 40)

# Desafio
# Imprima a contagem regressiva para o lançamento
# da estação espacial Brasilia-1
# formato: 10...9...8...7...6...5...4...3...2...1

contador = 10
while contador >= 1:
    print(contador, end = "...")
    contador -= 1
    if contador == 0:
        print("Fogo!!")

print()
print("=" * 40)
print("Fim da sequencia")
print("=" * 40)