# Este programa usa un for y un método de lista (pop)
# Sirve para que el usuario ingrese números y sumemos todos los números

# Lista vacía para guardar los números
numeros = []

# Pedimos 5 números al usuario y los agregamos a la lista
for i in range(5):
    num = int(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)  # append() agrega el número al final de la lista

# Inicializamos la suma
suma = 0

# Usamos un for para recorrer la lista
for i in range(len(numeros)):
    # pop() elimina el último elemento y lo devuelve
    n = numeros.pop()                               
    suma += n  # vamos sumando a partir del último elemnto devuelto 

# Mostramos el resultado
print("La suma de todos los números es:", suma)
