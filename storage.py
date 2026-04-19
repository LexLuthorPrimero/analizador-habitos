import json
import os

FILE = "data.json"


def cargar_datos():
    if not os.path.exists(FILE):
        return {}

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def guardar_datos(datos):
    with open(FILE, "w") as f:
        json.dump(datos, f, indent=4)