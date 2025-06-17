class ClimaSemanal:
    def __init__(self):
        # Encapsulación: Atributos privados
        self.__dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.__temperaturas = []

    # Método público para ingresar datos
    def ingresar_datos(self):
        print("\n" + "=" * 50)
        print("POO: REGISTRO DE TEMPERATURAS SEMANALES")
        print("=" * 50)
        
        for dia in self.__dias_semana:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    print("¡Error! Ingrese un valor numérico.")

    # Método público para calcular promedio
    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas) if self.__temperaturas else 0

    # Método público para mostrar resultados
    def mostrar_reporte(self):
        print("\nResumen semanal:")
        for idx, dia in enumerate(self.__dias_semana):
            print(f"  - {dia}: {self.__temperaturas[idx]}°C")
        print(f"\n>>> Promedio semanal: {self.calcular_promedio():.2f}°C")

# Clase derivada para extensión (Ejemplo de herencia)
class ClimaExtendido(ClimaSemanal):
    def __init__(self):
        super().__init__()
        self.__mes = ""

    # Polimorfismo: Extender funcionalidad
    def ingresar_datos(self):
        self.__mes = input("\nIngrese el mes: ")
        super().ingresar_datos()

    def mostrar_reporte(self):
        print(f"\nReporte del mes de {self.__mes}:")
        super().mostrar_reporte()

# Ejecución del programa
if __name__ == "__main__":
    semana = ClimaExtendido()  # Instancia de clase derivada
    semana.ingresar_datos()
    semana.mostrar_reporte()