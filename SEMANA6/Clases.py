class Lenguaje:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo    

    def description(self):
        print(f"{self.nombre} es un lenguaje de programacion {self.tipo}")
    
python = Lenguaje("Python", "multiparadigma")
c = Lenguaje("C", "procedural")
html = Lenguaje("HTML", "marcado")
python.description()
c.description()
html.description()
