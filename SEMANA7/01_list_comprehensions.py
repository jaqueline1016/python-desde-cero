# estructura de una list comprehension
# [expresión for elemento in iterable if condición] 

#tradicinal 
precios_brutos = [100, 250, 400, 50]
precios_con_iva1 = []

for p in precios_brutos:
    if p > 100:
        precios_con_iva1.append(p * 1.21)

#con list comprehension

precios_con_iva = [p * 1.21 for p in precios_brutos if p > 100]


usuarios = [("id_1", "Alice"), ("id_2", "Bob"), ("id_3", "Charlie")]
mapa_usuarios = {uid: nombre for uid, nombre in usuarios if nombre != "Bob"}

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

nueva_lista =  [n * 2 for n in lista_numeros if n % 2 == 0]

print(nueva_lista)