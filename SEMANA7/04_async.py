import asyncio

async def consultar_base_de_datos(id_usuario: int) -> dict:
    print(f"Buscando usuario {id_usuario} en la base de datos...")
    # Simulamos una espera de red (como un servidor real)
    await asyncio.sleep(2) 
    return {"id": id_usuario, "nombre": "Usuario Generico"}

async def main():
    # Lanzamos la tarea
    print("Inicio de la petición")
    usuario = await consultar_base_de_datos(1)
    print(f"Resultado: {usuario}")

# Para ejecutar una función async, usamos el disparador de asyncio
asyncio.run(main())