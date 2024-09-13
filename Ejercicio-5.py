#Lee un número por teclado e indica si es divisible entre 2 (resto = 0). Si no lo es, 
#también debemos indicarlo.


   # Tambien se puede escribir para resumir el codigo como: " numero1 = int(input("Ingrese un numero: ")); "   
numero1 = input("Ingrese un numero para verificar si es divisible por 2: ");  
numero1 = int(numero1); 

if numero1 % 2 == 0:
    print(f"El numero", numero1, "si es divisible por 2"); 
else:
    print(f"El numero",numero1, "no es divisible por 2"); 