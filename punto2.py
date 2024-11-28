def imprimir_impares(num1, num2): #imprimir los numeros impares entre num1 y num2
    for i in range (num1, num2 + 1 ):
        if i % 2 != 0: #si el numero no es divisible por 2 es impar
            print (i)


def main():
    try :
        num1 = int(input("ingrese el numero donde inicia el rango: "))
        num2 = int(input(" ingrese el numero donde termina el rango: "))
        if num1 > num2 :
            print("Error : el numero inicial debe ser menor o igual al numero final" )
        else:
            print(f"los numeros impares entre {num1} y {num2} son:  ") #nombro la funcion para imprimir los numeros impares
            imprimir_impares(num1,num2)
    except ValueError:
     print("Error: por favor ingrese numeros enteros ")
if __name__ == '__main__':
    main()
