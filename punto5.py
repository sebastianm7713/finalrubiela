def calcular_promedio():
    suma_notas = 0
    cantidad_notas = 0

    while True:
        try:
            nota = float(input(f"Ingrese la nota {cantidad_notas + 1}: "))
            
            # Verificar si la nota está en el rango de 0 a 5
            if 0 <= nota <= 5:
                suma_notas += nota
                cantidad_notas += 1
            else:
                print("Error: La nota debe estar en el rango de 0 a 5.")
            
            # Preguntar si desea ingresar más notas
            continuar = input("¿Desea ingresar otra nota? (s/n): ").lower()
            if continuar != 's':
                break
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la nota.")

    # Calcular el promedio
    if cantidad_notas > 0:
        promedio = suma_notas / cantidad_notas
        return promedio
    else:
        print("Error: No se ingresaron notas válidas.")
        return None

def determinar_aprobacion(promedio):
    if promedio >= 4.5:
        print(f"Felicidades, has aprobado con un promedio de {promedio:.2f}!")
    else:
        print(f"No has aprobado. Tu promedio es {promedio:.2f}. Necesitas un mínimo de 4.5 para aprobar.")

def main():
    promedio = calcular_promedio()
    
    if promedio is not None:
        determinar_aprobacion(promedio)

if __name__ == "__main__":
    main()