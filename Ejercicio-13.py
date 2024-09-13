num=int(input("Ingrese un numero para averiguar si es primo o no: "))
cont=0
cuenta=0
while cuenta<num:
    cuenta+=1
    if num % cuenta==0:
        cont+=1
    if cont>2:
        print("El numero no es primo.")
        break
    elif cuenta==num:
        print("El numero es primo.")