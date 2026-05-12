#diccionario de frutas
frutas = {
    "manzana": {"color": "rojo", "tamaño": "mediano"},
    "naranja": {"color": "naranja", "tamaño": "mediano"}
}

def imprimir_info_fruta():
    for fruta, info in frutas.items():
        print(f"{fruta}:")
        print(f"  Color: {info['color']}")
        print(f"  Tamaño: {info['tamaño']}")

imprimir_info_fruta()