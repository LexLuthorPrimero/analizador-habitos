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

    print("\nTotal:", calcular_total(habitos))
    print("Promedio:", round(calcular_promedio(habitos), 2))