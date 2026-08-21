import datetime

class AgendaCumpleanios:
    def __init__(self):
        self.cumpleanios = {}

    def agregar_amigo(self, nombre, fecha_str):
        """
        Añade un amigo a la agenda.
        fecha_str debe tener formato 'dd-mm-aaaa'
        """
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%d-%m-%Y").date()
            self.cumpleanios[nombre] = fecha
            print(f"Cumpleaños de {nombre} guardado para el {fecha.strftime('%d-%m-%Y')}")
        except ValueError:
            print("Formato de fecha incorrecto. Usa 'dd-mm-aaaa'.")

    def eliminar_amigo(self, nombre):
        if nombre in self.cumpleanios:
            del self.cumpleanios[nombre]
            print(f"{nombre} eliminado de la agenda.")
        else:
            print(f"{nombre} no se encontró en la agenda.")

    def mostrar_agenda(self):
        if not self.cumpleanios:
            print("La agenda está vacía.")
            return
        print("Agenda de cumpleaños:")
        for nombre, fecha in sorted(self.cumpleanios.items(), key=lambda x: (x[1].month, x[1].day)):
            print(f"{nombre}: {fecha.strftime('%d-%m-%Y')}")

    def cumpleanos_hoy(self):
        hoy = datetime.date.today()
        cumpleanieros = [nombre for nombre, fecha in self.cumpleanios.items()
                         if fecha.day == hoy.day and fecha.month == hoy.month]
        if cumpleanieros:
            print("Hoy cumplen años:")
            for nombre in cumpleanieros:
                print(f" - {nombre}")
        else:
            print("Nadie cumple años hoy.")

# Ejemplo de uso:
if __name__ == "__main__":
    agenda = AgendaCumpleanios()
    while True:
        print("\nOpciones: 1) Agregar 2) Eliminar 3) Mostrar agenda 4) Cumpleaños de hoy 5) Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            nombre = input("Nombre de tu amigo: ")
            fecha = input("Fecha de cumpleaños (dd-mm-aaaa): ")
            agenda.agregar_amigo(nombre, fecha)
        elif opcion == "2":
            nombre = input("Nombre del amigo a eliminar: ")
            agenda.eliminar_amigo(nombre)
        elif opcion == "3":
            agenda.mostrar_agenda()
        elif opcion == "4":
            agenda.cumpleanos_hoy()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

