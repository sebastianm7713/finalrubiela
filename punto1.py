def calcular_factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    try:
        n = int(input("Ingresa un número entero para calcular su factorial: "))
        resultado = calcular_factorial(n)
        print(f"El factorial de {n} es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

    