# condicionales 

# if, elif, else
edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Eres menor de edad")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")


# match 
color = input("Ingrese un color (rojo, verde, azul): ")
match color:
    case "rojo":
        print("El color es rojo")
    case "verde":
        print("El color es verde")
    case "azul":
        print("El color es azul")
    case _:
        print("Color no reconocido")