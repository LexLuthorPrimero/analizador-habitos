import json
import os
import pandas as pd

DATA_PATH = "data/data.json"


# -----------------------------
# LOAD RAW
# -----------------------------
def load_data() -> pd.DataFrame:
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame(columns=["fecha", "habito", "minutos"])

    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return pd.DataFrame(columns=["fecha", "habito", "minutos"])

    # caso correcto: lista de eventos
    if isinstance(data, list):
        return pd.DataFrame(data)

    # compatibilidad legacy: dict anidado
    if isinstance(data, dict):
        rows = []
        for fecha, habitos in data.items():
            if isinstance(habitos, dict):
                for habito, minutos in habitos.items():
                    rows.append({
                        "fecha": fecha,
                        "habito": habito,
                        "minutos": minutos
                    })
        return pd.DataFrame(rows)

    return pd.DataFrame(columns=["fecha", "habito", "minutos"])


# -----------------------------
# SAVE (FORMATO ÚNICO)
# -----------------------------
def save_data(df: pd.DataFrame):
    os.makedirs("data", exist_ok=True)

    df = df.copy()
    df["fecha"] = df["fecha"].astype(str)

    data = df.to_dict(orient="records")

    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)