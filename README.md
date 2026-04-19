# 📊 Habit Tracker Analytics

Sistema de análisis de hábitos personales basado en datos, construido con Python, Pandas y Streamlit.

El objetivo del proyecto es transformar registros simples de hábitos en métricas, patrones temporales e insights accionables sobre consistencia y productividad.

---

## 🧠 Problema

Registrar hábitos no es suficiente.  
El valor aparece cuando los datos se convierten en señales:

- ¿Qué hábitos son realmente consistentes?
- ¿Dónde se rompe la continuidad?
- ¿Existe progreso o estancamiento?
- ¿Qué actividad domina el comportamiento diario?

Este sistema responde esas preguntas mediante análisis automatizado.

---

## ⚙️ Arquitectura

El proyecto está dividido en tres capas:

### 1. Storage Layer
Persistencia de datos en JSON estructurado o formato plano normalizado.

### 2. Analysis Layer
Procesamiento con Pandas para:

- Limpieza y validación de datos
- Cálculo de métricas agregadas
- Detección de rachas
- Score de hábitos (frecuencia + continuidad + recencia)
- Análisis de tendencia temporal

### 3. Presentation Layer
Dashboard interactivo construido con Streamlit + Plotly.

---

## 📈 Features

### 📌 Métricas clave
- Total de minutos registrados
- Promedio diario
- Hábito dominante
- Día más productivo

### 🔥 Análisis de comportamiento
- Rachas de consistencia por hábito
- Score comparativo entre hábitos
- Tendencia general del sistema

### 📊 Visualización
- Minutos por hábito
- Evolución temporal
- Ranking de hábitos
- Series por actividad

---

## 🧮 Modelo de scoring

Cada hábito se evalúa con un score compuesto:

- Frecuencia de uso
- Longitud de rachas
- Recencia de actividad

Esto permite comparar hábitos activos vs hábitos esporádicos.

---

## 🛠 Stack

- Python
- Pandas
- Streamlit
- Plotly
- Matplotlib

---

## 🚀 Ejecución local

```bash
pip install -r requirements.txt
streamlit run app.py