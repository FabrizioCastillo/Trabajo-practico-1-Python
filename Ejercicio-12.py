a=True
while a==True:
    num=input("Ingresa un dia de la semana (numero).")
    num=int(num)
    if num > 1 and num <= 7:
        match num:
            case 1|2|3|4|5:
                print("Es un día laboral.")
                a=False
            case 6|7:
                print("No es un día laboral.")
                a=False