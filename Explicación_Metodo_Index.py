#Explicación método index, correspondiente a estructura de datos tipo list
#El método index() sirve para saber en qué posición (índice) está un elemento dentro de una lista.

# Este programa sirve para buscar dónde está un número en tu lista

# Primero vamos a crear nuestra lista vacía, donde iremos guardando los números
numeros = []

# Vamos a pedirle al usuario 5 números para llenar la lista
for i in range(5):
    # Le decimos qué número está ingresando
    num = int(input(f"Ingresa el número {i+1}: "))
    # Lo agregamos a la lista
    numeros.append(num)

# Mostramos toda la lista para que el usuario vea lo que puso
print("Tu lista quedó así:", numeros)

# Ahora le pedimos un número para buscarlo en la lista
buscar = int(input("¿Qué número quieres buscar en la lista? "))

# Revisamos si el número que puso el usuario está en la lista
if buscar in numeros:
    # Si está, usamos index() para saber en qué posición está
    posicion = numeros.index(buscar)
    print(f"El número {buscar} está en la posición {posicion}")
else:
    # Si no está, le decimos que no lo encontró
    print("Ese número no está en la lista")
