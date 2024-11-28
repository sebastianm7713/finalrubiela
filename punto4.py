def calcular_inversion(cantidad_invertir, interes_anual, anos):
    # Fórmula para calcular el capital obtenido en inversión con interés compuesto
    capital_final = cantidad_invertir * (1 + interes_anual / 100) ** anos
    return capital_final

def main():
    try:
        # Pedir al usuario los datos necesarios
        cantidad_invertir = float(input("Ingresa la cantidad de dinero a invertir: "))
        interes_anual = float(input("Ingresa el interés anual (en porcentaje): "))
        anos = int(input("Ingresa la cantidad de años de la inversión: "))
        
        # Calcular el capital final
        capital_obtenido = calcular_inversion(cantidad_invertir, interes_anual, anos)
        
        # Mostrar el resultado
        print(f"El capital obtenido después de {anos} años será: {capital_obtenido:.2f}")
    
    except ValueError:
        print("Error: Por favor, ingresa valores válidos.")

if __name__ == "__main__":
    main()
     