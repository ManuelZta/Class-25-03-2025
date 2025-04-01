def suma_impares(n):
    if n < 1:
        print("N debe ser un número entero positivo.")
        return
    
    suma = sum(i for i in range(1, n + 1, 2))
    print(f"La suma de los números impares entre 1 y {n} es: {suma}")

# Solicitar entrada del usuario
n = int(input("Ingrese un número entero positivo: "))
suma_impares(n)