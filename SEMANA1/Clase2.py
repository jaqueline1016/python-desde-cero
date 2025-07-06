#DATOS COMPUESTOS 

# Lista

lista = ["lucas",45, True, 485.658, "hola"]
print(lista)
print(lista[0]) # indice 0
print(lista[1]) # indice 1 

#- se pueden modificar 
lista[1] = "nuevo"


# TUPLAS 

tupla = ("lucas",45, True, 485.658, "hola")
# - no se pueden modificar 
print(tupla[0])
# se obtiene el dato con []


# Creando un conjunto Set
conjunto ={"lucas",45, True, 485.658, "hola"}
conjunto = {"esto si es valido "}
# - no tiene orden
# -no se pueden modifica elementos 
# - pero se puede cambiar 
# - no se puede acceder por indice 
# print(conjutno[1]) no se puede
# - no puede haber datos duplicados 
# - se puede accder  por medio de un buble 
print(conjunto)


#DICCIONARIO 

diccionario = { 
    "nombre": "jack",  #indice 0
    "canal": "prueba", #indice 1
    "numero": 45,       
    "bool": True,
    "decimal": 48.65,
    "dubplicado": "prueba"
}

print(diccionario["nombre"])
# -no tiene un corden 
# - estructura 
#  clave: valor
#  key: value
# - se separa comas si tiene mas elementos menos el ultimo elemento y si solo hay uno 

