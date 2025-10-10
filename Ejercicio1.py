# EJERCICIO 1

lista_original = list(range(1, 21))
print(f"Lista original (1 al 20): {lista_original}")

lista_pares_bucle = []
for numero in lista_original:

    if numero % 2 == 0:
        lista_pares_bucle.append(numero)

print(f"Lista resultante (solo pares): {lista_pares_bucle}")
