# 1. Lista inicial de tareas pendientes
tasks = ["Comprar víveres", "Lavar la ropa", "Estudiar Python", "Pagar la factura"]
print(f"Lista inicial de tareas: {tasks}")

# 2. Usar pop() sin índice (extrae y elimina el último elemento)
print("\n--- Tarea completada (la última) ---")
last_task_done = tasks.pop()
print(f"Tarea completada: '{last_task_done}'")
print(f"Lista de tareas restantes: {tasks}")


# 3. Usar pop() con un índice (extrae y elimina un elemento específico, e.g., el índice 0)
print("\n--- Tarea completada (la primera) ---")
first_task_done = tasks.pop(0)
print(f"Tarea completada: '{first_task_done}'")
print(f"Lista de tareas restantes: {tasks}")



# 1. Lista inicial de números
numbers = [10, 20, 30, 40, 50]
print(f"Lista original: {numbers}")

# 2. Usar reverse() para invertir el orden de la lista
numbers.reverse()

# 3. Mostrar la lista después de la inversión
print(f"Lista después de usar reverse(): {numbers}")


# 4. segundo ejemplo
words = ["manzana", "banana", "cereza"]
print(f"\nLista de palabras original: {words}")

# 5. Invertir la lista de palabras
words.reverse()
print(f"Lista de palabras invertida: {words}")

