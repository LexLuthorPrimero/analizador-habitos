import streamlit as st
import pandas as pd
import plotly.express as px
from src.analysis import run_analysis
from src.storage import load_data

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="Habit Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Habit Analytics Dashboard")
st.caption("Análisis de hábitos basado en datos reales")

# -----------------------------
# CACHE
# -----------------------------
@st.cache_data
def load_and_prepare():
    df = load_data()

    if df.empty:
        st.warning("No hay datos cargados.")
        st.stop()

    if df.empty:
        return df

    df["minutos"] = pd.to_numeric(df["minutos"], errors="coerce")
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    return df.dropna()

df = load_and_prepare()

if df.empty:
    st.warning("No hay datos válidos.")
    st.stop()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Filtros")

habitos = df["habito"].unique()

habito_sel = st.sidebar.multiselect(
    "Hábitos",
    habitos,
    default=habitos
)

df = df[df["habito"].isin(habito_sel)]

if df.empty:
    st.warning("Sin datos para los filtros.")
    st.stop()

# -----------------------------
# ANALYSIS
# -----------------------------
results = run_analysis(df)

if "error" in results:
    st.error(results["error"])
    st.stop()

metrics = results["metrics"]

# -----------------------------
# KPIs
# -----------------------------
st.subheader("📌 Métricas clave")

col1, col2, col3 = st.columns(3)

col1.metric("Minutos totales", metrics["total_minutos"])
col2.metric("Promedio diario", metrics["promedio_diario"])
col3.metric("Hábito dominante", metrics["habito_dominante"])

# -----------------------------
# CHARTS
# -----------------------------
st.subheader("📈 Visualizaciones")

col1, col2 = st.columns(2)

# --- barras
with col1:
    df_bar = (
        df.groupby("habito")["minutos"]
        .sum()
        .reset_index()
        .sort_values("minutos", ascending=False)
    )

    fig_bar = px.bar(
        df_bar,
        x="habito",
        y="minutos",
        title="Minutos por hábito"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

# --- evolución
with col2:
    df_line = df.sort_values("fecha")

    fig_line = px.line(
        df_line,
        x="fecha",
        y="minutos",
        color="habito",
        title="Evolución temporal"
    )

    st.plotly_chart(fig_line, use_container_width=True)

# -----------------------------
# SCORE VISUAL
# -----------------------------
st.subheader("🏆 Score de hábitos")

scores_df = (
    pd.DataFrame.from_dict(results["scores"], orient="index")
    .reset_index()
    .rename(columns={"index": "habito", 0: "score"})
)

fig_score = px.bar(
    scores_df,
    x="habito",
    y="score",
    title="Ranking de hábitos"
)

st.plotly_chart(fig_score, use_container_width=True)

# -----------------------------
# TENDENCIA
# -----------------------------
st.subheader("📊 Tendencia")

tendencia = results["trend"].get("tendencia", "insuficiente")

if tendencia == "subiendo":
    st.success("Tendencia en aumento")
elif tendencia == "bajando":
    st.error("Tendencia en descenso")
else:
    st.info("Tendencia estable o insuficiente")

# -----------------------------
# RACHAS
# -----------------------------
st.subheader("🔥 Rachas")

st.dataframe(
    pd.DataFrame(
        list(results["streaks"].items()),
        columns=["Hábito", "Racha máxima"]
    )
)

# -----------------------------
# DATA
# -----------------------------
with st.expander("Ver datos crudos"):
    st.dataframe(df)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Stack: Python · Pandas · Plotly · Streamlit")