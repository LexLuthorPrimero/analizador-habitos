from utils import mostrar_resumen

def pedir_habitos():
    habitos = {}

    print("🧠 ANALIZADOR DE HÁBITOS")
    print("Escribí 'fin' para terminar\n")

    while True:
        nombre = input("Nombre del hábito: ")

        if nombre.lower() == "fin":
            break

        try:
            minutos = int(input("Minutos dedicados: "))
        except ValueError:
            print("⚠️ Ingresá un número válido")
            continue

        habitos[nombre] = minutos

    return habitos


def main():
    habitos = pedir_habitos()

    if len(habitos) == 0:
        print("No se ingresaron hábitos.")
        return

    mostrar_resumen(habitos)


if __name__ == "__main__":
    main()