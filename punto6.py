def convertir_dolares_a_pesos(dolares, tasa_de_cambio):
    # Realiza la conversión de dólares a pesos
    return dolares * tasa_de_cambio

def main():
    tasa_de_cambio = 3.934  # Tasa de cambio fija de dólares a pesos
    
    while True:
        try:
            # Pedir al usuario la cantidad de dólares a convertir
            dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
            
            # Realizar la conversión
            pesos = convertir_dolares_a_pesos(dolares, tasa_de_cambio)
            
            # Mostrar el resultado de la conversión
            print(f"{dolares} dólares equivalen a {pesos:.2f} pesos .")
        
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la cantidad de dólares.")
        
        # Preguntar si desea realizar otra conversión
        seguir = input("¿Desea realizar otra conversión? (s/n): ").lower()
        
        if seguir != 's':
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()