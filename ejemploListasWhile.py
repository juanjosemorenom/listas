lista_super = ["leche", "pan", "jabon", "papel", "Don_julio"]

print("Empezar compra", lista_super)

while lista_super:
  articulo_actual = lista_super.pop(0)
  print(f"Tomando: {articulo_actual}")

print("\n¡Lista vacía! Hemos terminado de comprar.")
print("Lista final:", lista_super)

 