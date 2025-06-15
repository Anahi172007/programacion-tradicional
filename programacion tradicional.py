# Programa Tradicional para calcular el promedio semanal del clima

def ingresar_temperaturas():
    """
    Solicita al usuario que ingrese las temperaturas de los 7 días de la semana.
    Devuelve una lista con las temperaturas.
    """
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula y devuelve el promedio de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)

def main():
    """
    Función principal que organiza el flujo del programa.
    """
    print("=== Promedio Semanal del Clima (Modo Tradicional) ===")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
