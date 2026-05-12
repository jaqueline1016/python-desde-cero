from typing import List, Dict

# Definimos la función con pistas de tipo
def obtener_nombres_mayores(lista_db: List[Dict[str, any]]) -> List[str]:
    # 1. Recibimos una lista de diccionarios (pueden tener strings, ints, etc. -> 'any')
    # 2. Usamos una List Comprehension para filtrar
    resultado = [usuario["nombre"] for usuario in lista_db if usuario["edad"] >= 18]
    
    # 3. Devolvemos una lista de strings
    return resultado

# Datos de prueba (Simulando una respuesta de base de datos)
datos_crudos = [
    {"nombre": "Alice", "edad": 25},
    {"nombre": "Bob", "edad": 17},
    {"nombre": "Charlie", "edad": 30}
]

# Ejecución
nombres = obtener_nombres_mayores(datos_crudos)
print(nombres)  # Salida: ['Alice', 'Charlie']