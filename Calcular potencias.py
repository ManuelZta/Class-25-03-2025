def calcular_potencias(n):
    if not (1 <= n <= 9):
        print("El valor de n debe estar entre 1 y 9.")
        return
    
    print(f"Resultados de {n}^x desde x = 0 hasta x = {n}:")
    for x in range(n + 1):
        resultado = n ** x
        print(f"{n}^{x} = {resultado}")

# Solicitar entrada del usuario
n = int(input("Ingrese un número entero positivo (máximo 9): "))
calcular_potencias(n)