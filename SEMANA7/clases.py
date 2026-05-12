class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre 
        self.__precio = precio # atributo privado

    def obtener_precio_final(self, impuesto: float):
        return self.__precio * (1 + impuesto)   
    
pan = Producto("Pan", 1.5)
print(f"Producto: {pan.nombre}, Total: {pan.obtener_precio_final(0.07)}")
