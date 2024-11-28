def calcular_calificacion_final(nota1, nota2, nota3):
    # Calcula la calificación final utilizando los porcentajes especificados
    calificacion = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)
    return calificacion

def evaluar_aprobacion(calificacion):
    # Determina si la calificación es suficiente para aprobar
    if calificacion >= 4:
        return "APROBADO"
    else:
        return "REPROBADO"

def main():
    # Solicitar los datos del usuario
    nombre = input("Ingresa tu nombre: ")
    asignatura = input("Ingresa la asignatura: ")
    
    # Pedir las tres notas de los exámenes
    while True:
        try:
            nota1 = float(input("Ingresa la nota del primer examen (0-5): "))
            nota2 = float(input("Ingresa la nota del segundo examen (0-5): "))
            nota3 = float(input("Ingresa la nota del último examen (0-5): "))
            
            # Verificar que las notas estén dentro del rango permitido
            if 0 <= nota1 <= 5 and 0 <= nota2 <= 5 and 0 <= nota3 <= 5:
                break
            else:
                print("Error: Las notas deben estar entre 0 y 5. Intenta nuevamente.")
        except ValueError:
            print("Error: Ingresa un valor válido para las notas.")
    
    # Calcular la calificación final
    calificacion_final = calcular_calificacion_final(nota1, nota2, nota3)
    
    # Evaluar si aprueba o reprueba
    resultado = evaluar_aprobacion(calificacion_final)
    
    # Mostrar los resultados
    print(f"\nNombre del aprendiz: {nombre}")
    print(f"Asignatura: {asignatura}")
    print(f"Calificación final: {calificacion_final:.2f}")
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()