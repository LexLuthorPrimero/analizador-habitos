from src.storage import add_entry, load_data
from src.analysis import get_dataframe, compute_insights
from src.analysis import run_analysis
from src.storage import load_data
def main():
    while True:
        print("\n1. Cargar datos")
        print("2. Ver análisis")
        print("3. Salir")

        opcion = input("Elegí: ")

        if opcion == "1":
            while True:
                habito = input("Hábito (fin para salir): ")
                if habito == "fin":
                    break
                minutos = int(input("Minutos: "))
                add_entry(habito, minutos)

        elif opcion == "2":
            data = load_data()
            df = get_dataframe(data)
            print(df)

            insights = compute_insights(df)
            print("\nINSIGHTS")
            print(insights)

        elif opcion == "3":
            break

if __name__ == "__main__":
    main()