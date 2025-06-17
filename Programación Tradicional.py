# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []
    
    # Solicitar temperatura para cada día
    for dia in dias_semana:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("¡Error! Ingrese un valor numérico.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temps):
    return sum(temps) / len(temps) if temps else 0

# Función principal
def main():
    print("\n" + "=" * 50)
    print("PROGRAMACIÓN TRADICIONAL: PROMEDIO SEMANAL DE CLIMA")
    print("=" * 50)
    
    # Obtener datos y calcular resultado
    temps_semana = ingresar_temperaturas()
    promedio = calcular_promedio(temps_semana)
    
    # Mostrar resultados
    print("\nResumen semanal:")
    for i, temp in enumerate(temps_semana):
        print(f"  - Día {i+1}: {temp}°C")
    print(f"\n>>> Promedio semanal: {promedio:.2f}°C")

# Ejecutar programa
if __name__ == "__main__":
    main()