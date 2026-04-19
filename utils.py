def calcular_total(habitos):
    return sum(habitos.values())


def calcular_promedio(habitos):
    if len(habitos) == 0:
        return 0
    return sum(habitos.values()) / len(habitos)


def mostrar_resumen(habitos):
    print("\n📊 RESUMEN DEL DÍA")
    print("-------------------")

    for nombre, minutos in habitos.items():
        print(f"{nombre}: {minutos} min")

    total = calcular_total(habitos)
    promedio = calcular_promedio(habitos)

    print("\nTotal de minutos:", total)
    print("Cantidad de hábitos:", len(habitos))
    print("Promedio por hábito:", round(promedio, 2))