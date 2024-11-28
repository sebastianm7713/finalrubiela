def jubilarse(edad, sexo):
    # Verificar las condiciones de jubilación según el sexo
    if sexo.lower() == 'hombre':
        if edad >= 63:
            return "¡Ya puedes jubilarte anciano!"
        else:
            return "Aún no puedes jubilarte niño."
    elif sexo.lower() == 'mujer':
        if edad > 54:
            return "¡Ya puedes jubilarte anciana!"
        else:
            return "Aún no puedes jubilarte niña."
    else:
        return "Sexo no válido. Por favor, ingresa 'hombre' o 'mujer'."

def main():
    # Solicitar la edad y el sexo al usuario
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad <= 0:
                print("Por favor, ingresa una edad válida mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: Ingresa un número válido para la edad.")
    
    while True:
        sexo = input("Ingresa tu sexo (hombre/mujer): ").strip().lower()
        if sexo == 'hombre' or sexo == 'mujer':
            break
        else:
            print("Error: Por favor, ingresa 'hombre' o 'mujer'.")
    
    # Evaluar si puede jubilarse
    resultado = jubilarse(edad, sexo)
    print(resultado)

if __name__ == "__main__":
    main()