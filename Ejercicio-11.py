contraseña = "Ejemplo"
for num in range(0,3):
    contraseñaingresada = input("Ingrese la contraseña: ")
    if contraseñaingresada == contraseña:
        print("Acceso Correcto")
        break
else:
        print("El acceso se ha bloqueado después de los 3 intentos.")
