def mostrar_numeros_con_salto():
    numeros = ""  # Cadena para almacenar los números
    for num in range(1, 31):
        # Añadir cada número y un espacio a la cadena
        numeros += str(num) + " "
        if num % 7 == 0:
            numeros += "\n"  # Salto de línea
        
    print(numeros)  # Imprimir toda la cadena al final

def main():
    mostrar_numeros_con_salto()

if __name__ == "__main__":
    main()
                