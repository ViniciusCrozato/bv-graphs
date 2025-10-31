import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
from collections import Counter

st.set_page_config(page_title="Alinhamento Produto vs Demanda")

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
    fig, ax = plt.subplots(figsize=(4, 4))
    notas_redacao = np.random.randint(1, 6, size=100)
    sns.histplot(
        notas_redacao, 
        bins=np.arange(1, 7) - 0.5,  
        ax=ax, 
        color="skyblue", 
        edgecolor="black"
    )
    ax.set_title("Alinhamento Redação (1-5)")
    ax.set_xlabel("Nota (1=ruim, 5=excelente)")
    ax.set_ylabel("Quantidade")
    ax.set_xticks([1, 2, 3, 4, 5])  
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
    materias = ["MAT", "PORT", "HIS", "FIS", "QUIM", "BIO", "GEO"]
    dificuldades = np.random.choice(materias, size=100, p=[0.25, 0.2, 0.1, 0.15, 0.1, 0.1, 0.1])

    
    contagem = Counter(dificuldades)
    materias_ordenadas = [m for m, _ in contagem.most_common()]  

    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(
        x=dificuldades,
        order=materias_ordenadas,
        ax=ax,
        color="salmon",
        edgecolor="black"
    )
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
ax.pie(contagem_nota, labels=contagem_nota.index, autopct="%1.1f%%", startangle=90, colors=[ "#F44336","#4CAF50"])
ax.set_title("Nota suficiente?")
st.pyplot(fig)

# ========= 5. Indicação do BuscaVest =========
st.header("5. Chance de recomendar (NPS-like)")

indicacao = np.random.randint(1, 11, size=100)

fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(indicacao, bins=np.arange(1,12) - 0.5, ax=ax, color="purple", edgecolor="black")
ax.set_title("Chance de recomendar (1-10)")
ax.set_xlabel("Nota")
ax.set_ylabel("Quantidade") 
ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
st.pyplot(fig)

st.divider()

st.write("""
# Alinhamento entre produto e demanda do ensino superior

Esse painel nos mostra como nosso produto foi recebido, o quanto conseguimos nos inserir no mercado e se coincidiu com as expectativas.

## Cenários 

Nas tabelas de feedback, temos 3 possíveis cenários, que ocorrem após o período de vestibulares.
- Os usuários que voltam ao site, após finalizar as provas e usufruem ainda do produto.
- Os usuários que não voltam para visitar o site, mas ainda mantêm algum vínculo.
- Os usuários que não voltam ao site e não mantêm nenhum vínculo.

_(O vínculo pode ser pela rede social ou pela assinatura do plano das rotas de estudos.)_

## Método que utilizamos

Estamos utilizando um formulário com perguntas estratégicas para avaliar a contribuição e o quanto conseguimos alcançar nosso objetivo com o usuário.

_**Na maioria das perguntas, utilizamos listagem de respostas em texto, pois pode ter alguma informação ou algo importante a ser compartilhado.**_

- 1ª Pergunta:   
    - **Os simulados de redação e os temas apresentados se alinharam com o que houve no vestibular?**
        - Utilizamos um histograma de 1 a 5, para saber o quão próximo e útil abordamos os assuntos: 1 = pouco alinhado, 5 = muito alinhado.
        - Listagem de respostas.
- 2ª Pergunta: 
    - **Qual matéria teve mais dificuldade no vestibular?**
        - Histograma das matérias presentes.
        - Listagem de respostas.
- 3ª Pergunta:
    - **Qual formato de estudo mais contribuiu para o seu preparo? (simulados, videoaulas, podcasts, leituras, laboratórios de aprendizado)**
        - Utilizamos o pie chart, com uma visualização mais simples, que nos demonstra qual método podemos melhorar e qual teve o melhor resultado.
        - Listagem de respostas.
- 4ª Pergunta:
    - **Sua nota foi suficiente para o curso ou instituição que tinha em plano?**
        - Pie chart, forma simples de visualizar a porcentagem de "SIM" e "NÃO".
- 5ª Pergunta:
    - **Qual a chance de você indicar as trilhas do BuscaVest para um amigo ou conhecido? (1-10)**
        - Histograma de 1 a 10, para avaliação de nossos serviços.
""")