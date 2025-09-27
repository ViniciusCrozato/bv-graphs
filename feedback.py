import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Alinhamento Produto vs Demanda", layout="wide")

# ========= MOCK DATA =========
np.random.seed(42)

emails = [f"user{i}@exemplo.com" for i in range(1, 51)]
sentimentos = ["positivo", "neutro", "negativo"]
respostas_preview = [
    "Gostei bastante, mas poderia ter mais exemplos.",
    "Achei confuso em alguns pontos.",
    "Excelente! Caiu parecido na prova.",
    "Faltou abordar alguns temas recentes.",
    "Boa experiência geral, mas dá para melhorar."
]

def gerar_respostas(n=20):
    return [
        {
            "email": random.choice(emails),
            "sentimento": random.choice(sentimentos),
            "preview": random.choice(respostas_preview)
        }
        for _ in range(n)
    ]

# ========= 1. Redação =========
st.title("📊 Dashboard 4 - Alinhamento entre Produto e Demanda do Ensino Superior")

st.header("1. Simulados de redação vs vestibular")

col1, col2 = st.columns([2, 1])

with col1:
    notas_redacao = np.random.randint(1, 6, size=100)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(notas_redacao, bins=5, ax=ax, color="skyblue", edgecolor="black")
    ax.set_title("Alinhamento Redação (1-5)")
    ax.set_xlabel("Nota (1=ruim, 5=excelente)")
    ax.set_ylabel("Quantidade")
    st.pyplot(fig)

with col2:
    st.subheader("Feedbacks")
    for r in gerar_respostas(5):
        with st.expander(f"{r['email']} - ({r['sentimento']})"):
            st.write(r["preview"])

# ========= 2. Matéria com mais dificuldade =========
st.header("2. Matéria com mais dificuldade")

col1, col2 = st.columns([2, 1])

with col1:
    materias = ["Matemática", "Português", "História", "Física", "Química", "Biologia", "Geografia"]
    dificuldades = np.random.choice(materias, size=100, p=[0.25,0.2,0.1,0.15,0.1,0.1,0.1])
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(dificuldades, ax=ax, color="salmon", edgecolor="black")
    ax.set_title("Matérias mais difíceis")
    ax.set_xlabel("Matéria")
    ax.set_ylabel("Quantidade")
    st.pyplot(fig)

with col2:
    st.subheader("Respostas dos usuários")
    for r in gerar_respostas(5):
        with st.expander(f"{r['email']} - ({r['sentimento']})"):
            st.write(r["preview"])

# ========= 3. Formato de estudo =========
st.header("3. Formato de estudo mais útil")

col1, col2 = st.columns([2, 1])

with col1:
    formatos = ["Simulados", "Videoaulas", "Podcasts", "Leituras", "Laboratórios"]
    contagens = np.random.randint(10, 50, size=len(formatos))
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(contagens, labels=formatos, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set2"))
    ax.set_title("Contribuição por formato de estudo")
    st.pyplot(fig)

with col2:
    st.subheader("Feedbacks de como melhorar")
    for r in gerar_respostas(5):
        with st.expander(f"{r['email']} - ({r['sentimento']})"):
            st.write(r["preview"])

# ========= 4. Nota suficiente =========
st.header("4. Nota suficiente para curso/instituição")

respostas_nota = np.random.choice(["Sim", "Não"], size=100, p=[0.6, 0.4])
contagem_nota = pd.Series(respostas_nota).value_counts()

fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(contagem_nota, labels=contagem_nota.index, autopct="%1.1f%%", startangle=90, colors=["#4CAF50", "#F44336"])
ax.set_title("Nota suficiente?")
st.pyplot(fig)

# ========= 5. Indicação do BuscaVest =========
st.header("5. Chance de recomendar (NPS-like)")

indicacao = np.random.randint(1, 11, size=100)

fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(indicacao, bins=10, ax=ax, color="purple", edgecolor="black")
ax.set_title("Chance de recomendar (1-10)")
ax.set_xlabel("Nota")
ax.set_ylabel("Quantidade")
st.pyplot(fig)
