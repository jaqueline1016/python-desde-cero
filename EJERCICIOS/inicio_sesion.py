username =  input("Ingrese su nombre de usuario: ")

if len(username) >= 12:
    print("El nombre de usuario es demasiado largo.")
elif not username.find(" ") == -1:
    print("El nombre de usuario no debe contener espacios.")
elif not username.isalpha():
    print("El nombre de usuario solo debe contener letras.")
else:
    print(f"Bienvenido, {username}!")