def evaluar_calificacion(calificacion):
    # Comprobamos si la calificación es aprobatoria o reprobatoria
    if calificacion < 7:
        return "REPROBADO"
    else:
        return "APROBADO"

def main():
    # Ingresar los datos
    nombre = input("Ingresa el nombre del aprendiz: ")
    asignatura = input("Ingresa la asignatura: ")
    
    while True:
        try:
            calificacion = float(input("Ingresa la calificación final (1-10): "))
            
            # Verificar que la calificación esté dentro del rango válido
            if 1 <= calificacion <= 10:
                break
            else:
                print("Error: La calificación debe estar entre 1 y 10.")
        except ValueError:
            print("Error: Ingresa un número válido para la calificación.")
    
    # Evaluar la calificación
    resultado = evaluar_calificacion(calificacion)
    
    # Mostrar los resultados
    print(f"\nNombre del aprendiz: {nombre}")
    print(f"Asignatura: {asignatura}")
    print(f"Calificación final: {calificacion}")
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()