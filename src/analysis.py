import pandas as pd


# -----------------------------
# PREPARACIÓN
# -----------------------------
def prepare(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df["minutos"] = pd.to_numeric(df["minutos"], errors="coerce")

    return df.dropna()


# -----------------------------
# MÉTRICAS
# -----------------------------
def compute_metrics(df):
    total_por_dia = df.groupby("fecha")["minutos"].sum()
    total_por_habito = df.groupby("habito")["minutos"].sum()

    return {
        "total_minutos": int(df["minutos"].sum()),
        "promedio_diario": round(total_por_dia.mean(), 2) if not total_por_dia.empty else 0,
        "habito_dominante": total_por_habito.idxmax() if not total_por_habito.empty else None,
        "dia_mas_productivo": str(total_por_dia.idxmax().date()) if not total_por_dia.empty else None,
    }


# -----------------------------
# RACHAS
# -----------------------------
def compute_streaks(df):
    result = {}

    for habito, g in df.groupby("habito"):
        fechas = g["fecha"].drop_duplicates().sort_values()

        best = 1
        cur = 1

        for i in range(1, len(fechas)):
            if (fechas.iloc[i] - fechas.iloc[i - 1]).days == 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1

        result[habito] = best

    return result


# -----------------------------
# SCORE
# -----------------------------
def compute_scores(df):
    hoy = pd.to_datetime("today").normalize()

    raw = {}

    for habito, g in df.groupby("habito"):
        fechas = g["fecha"].drop_duplicates().sort_values()

        freq = len(fechas)

        best = 1
        cur = 1

        for i in range(1, len(fechas)):
            if (fechas.iloc[i] - fechas.iloc[i - 1]).days == 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1

        last = fechas.iloc[-1]
        recencia = max(0, 1 - (hoy - last).days / 7)

        raw[habito] = {
            "freq": freq,
            "streak": best,
            "recencia": recencia
        }

    max_f = max(v["freq"] for v in raw.values()) if raw else 1
    max_s = max(v["streak"] for v in raw.values()) if raw else 1

    scores = {}

    for h, v in raw.items():
        score = (
            0.4 * (v["freq"] / max_f) +
            0.3 * (v["streak"] / max_s) +
            0.3 * v["recencia"]
        ) * 100

        scores[h] = round(score, 2)

    return scores


# -----------------------------
# TENDENCIA
# -----------------------------
def compute_trend(df):
    daily = df.groupby("fecha")["minutos"].sum().sort_index()
    diff = daily.diff().dropna()

    if diff.empty:
        return {"tendencia": "insuficiente"}

    mean = diff.mean()

    if mean > 0:
        return {"tendencia": "subiendo"}
    elif mean < 0:
        return {"tendencia": "bajando"}
    else:
        return {"tendencia": "estable"}


# -----------------------------
# ORQUESTADOR
# -----------------------------
def run_analysis(df):
    df = prepare(df)

    if df.empty:
        return {"error": "Datos inválidos"}

    return {
        "metrics": compute_metrics(df),
        "streaks": compute_streaks(df),
        "scores": compute_scores(df),
        "trend": compute_trend(df),
    }