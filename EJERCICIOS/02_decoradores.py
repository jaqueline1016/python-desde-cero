def avisar_limpieza(funcion_original):
    def envoltura():
        print("Limpiando datos innecesarios...")
        funcion_original()
        print("¡Limpieza terminada!")   
    return envoltura

@avisar_limpieza
def crear_lista_pares():
    pares = [n for n in range(20) if n % 2 == 0]
    print(pares)

crear_lista_pares()

#nivel senior
def avisar_limpieza(funcion_original):
    def envoltura(*args, **kwargs): # Acepta cualquier cantidad de parámetros
        print("Limpiando datos innecesarios...")
        resultado = funcion_original(*args, **kwargs) # Se los pasa a la original
        print("¡Limpieza terminada!")
        return resultado # Devuelve el resultado de la función original
    return envoltura

@avisar_limpieza
def crear_lista_pares(limite):
    pares = [n for n in range(limite) if n % 2 == 0]
    print(pares)

crear_lista_pares(10) # Ahora puedes pasarle el 10 sin que el decorador rompa el código
