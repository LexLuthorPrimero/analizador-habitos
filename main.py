from utils import mostrar_resumen
from storage import cargar_datos, guardar_datos
from datetime import date


def pedir_habitos():
    habitos = {}

    print("🧠 ANALIZADOR DE HÁBITOS")
    print("Escribí 'fin' para terminar\n")

    while True:
        nombre = input("Hábito: ")

        if nombre.lower() == "fin":
            break

        try:
            minutos = int(input("Minutos: "))
        except ValueError:
            print("Número inválido")
            continue

        habitos[nombre] = minutos

    return habitos


def main():
    datos = cargar_datos()
    hoy = str(date.today())

    habitos = pedir_habitos()

    if not habitos:
        print("Sin datos ingresados")
        return

    datos[hoy] = habitos
    guardar_datos(datos)

    mostrar_resumen(habitos)

    print("\n📅 Historial guardado correctamente")


if __name__ == "__main__":
    main()