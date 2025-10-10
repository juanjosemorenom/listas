import random

lista_numeros = []
for _ in range(10):
    numero_aleatorio = random.randint(1, 10)
    lista_numeros.append(numero_aleatorio)

print("Lista de 10 números aleatorios:", lista_numeros)

print("\nResultados:")
print("------------------------------")
print("| Número | Cuadrado | Cubo   |")
print("------------------------------")

for numero in lista_numeros:

    cuadrado = numero ** 2

    cubo = numero ** 3
    
    print(f"| {numero:^6} | {cuadrado:^8} | {cubo:^6} |")
