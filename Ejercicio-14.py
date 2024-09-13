import random
a = random.randint(0, 100) # Genera un número entero aleatorio entre 1 y 100
n = int(input("Adivine el número entero aleatorio entre 0 y 100: "))
while True:
    intentos = intentos + 1  #contador de intentos
    if n > a:
        print("Muy grande.")
    elif n < a:
        print("Muy pequeño.")
    else:
        print(f"¡Número correcto! Acertado en {intentos} intentos.")
        break