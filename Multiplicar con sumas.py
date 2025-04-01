def multiplicar_bajo_suma(a, b):
    resultado = 0
    for _ in range(abs(b)):  # Repetir la suma 'b' veces
        resultado += abs(a)
    
    # Ajustar el signo si uno de los números es negativo
    if (a < 0) ^ (b < 0):  
        resultado = -resultado
        
    return resultado

# Bucle para ejecutar múltiples veces
while True:
    a = int(input("Ingrese el número entero: "))
    b = int(input("Ingrese el las veces que se sumara el primer número: "))
    resultado = multiplicar_bajo_suma(a, b)
    print(f"El resultado de {a} x {b} es: {resultado}")
    
    opcion = input("¿Desea realizar otra multiplicación? (s/n): ").strip().lower()
    if opcion != 's':
        print("Saliendo del programa. ¡Hasta pronto!")
        break