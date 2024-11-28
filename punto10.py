def calcular_pago(precio):
    # Verificar si el precio es mayor a $20,000 y aplicar descuento del 20%
    if precio > 20000:
        descuento = precio * 0.20
        precio_final = precio - descuento
        return precio_final
    else:
        return precio

def main():
    # Solicitar el precio del producto al cliente
    while True:
        try:
            precio = float(input("Ingresa el precio del producto: $"))
            if precio > 0:
                break
            else:
                print("Error: El precio debe ser un valor positivo.")
        except ValueError:
            print("Error: Ingresa un valor numérico válido para el precio.")

    # Calcular el precio final
    precio_final = calcular_pago(precio)

    # Mostrar el resultado
    print(f"El precio final a pagar es: ${precio_final:.2f}")

if __name__ == "__main__":
    main()