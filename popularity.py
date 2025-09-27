
import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cursos/IES/Vest mais buscados")

# ========= MOCK DATA =========
np.random.seed(42)

instituicoes = [
    "Universidade de São Paulo (USP)",
    "Universidade Estadual de Campinas (UNICAMP)",
    "Universidade Estadual Paulista (UNESP)",
    "Universidade Federal do Rio de Janeiro (UFRJ)",
    "Universidade Federal de Minas Gerais (UFMG)",
    "Universidade Federal do Rio Grande do Sul (UFRGS)",
    "Universidade Federal do Paraná (UFPR)",
    "Universidade Federal de Santa Catarina (UFSC)",
    "Universidade Federal de Pernambuco (UFPE)",
    "Universidade Federal da Bahia (UFBA)",
    "Universidade Federal de Brasília (UnB)",
    "Universidade Federal do Ceará (UFC)",
    "Universidade Federal de Goiás (UFG)",
    "Universidade Federal do Pará (UFPA)",
    "Universidade Federal do Rio Grande do Norte (UFRN)",
    "Universidade Estadual do Ceará (UECE)",
    "Universidade Estadual do Rio de Janeiro (UERJ)",
    "Universidade Federal de Uberlândia (UFU)",
    "Universidade Federal de Juiz de Fora (UFJF)",
    "Universidade Federal de São Carlos (UFSCar)"
]

areas = ["Engenharia", "Saúde", "Direito", "Educação", "TI", "Artes", "Administração"]
cursos = [f"Curso {i}" for i in range(1, 51)]
vestibulares = ["ENEM", "Fuvest", "Unicamp", "UFMG", "UERJ", "UFBA", "UECE", "UNICENTRO"]

# buscas mock
df_cursos = pd.DataFrame({
    "curso": np.random.choice(cursos, 300),
    "instituicao": np.random.choice(instituicoes, 300),
    "area": np.random.choice(areas, 300)
})
df_cursos["buscas"] = np.random.randint(10, 200, df_cursos.shape[0])

df_instituicoes = df_cursos.groupby("instituicao")["buscas"].sum().reset_index()
df_vestibulares = pd.DataFrame({
    "vestibular": vestibulares,
    "buscas": np.random.randint(100, 1000, len(vestibulares))
})

# ========= DASHBOARD =========
st.title("📊 Dashboard 1 - Cursos, Instituições e Vestibulares mais buscados")

# --- 1. Cursos mais buscados ---
st.subheader("🎓 Cursos mais buscados")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Agrupados por Instituição**")
    cursos_por_inst = df_cursos.groupby("instituicao")["buscas"].sum().sort_values(ascending=False).head(10)
    st.table(cursos_por_inst)

with col2:
    st.markdown("**Agrupados por Área do Conhecimento**")
    cursos_por_area = df_cursos.groupby("area")["buscas"].sum().sort_values(ascending=False)
    st.table(cursos_por_area)

# --- 2. IES mais buscadas ---
st.subheader("🏛️ Instituições mais buscadas")
top_n_ies = st.slider("Quantas instituições exibir:", min_value=5, max_value=20, value=10)

top_inst = df_instituicoes.sort_values("buscas", ascending=False).head(top_n_ies)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=top_inst, x="buscas", y="instituicao", palette="viridis", ax=ax, orient="h")
ax.set_title(f"Top {top_n_ies} Instituições mais buscadas")
ax.set_xlabel("Quantidade de buscas")
ax.set_ylabel("Instituição")
st.pyplot(fig)

# --- 3. Vestibulares mais buscados ---
st.subheader("📑 Vestibulares mais buscados")
top_n_vest = st.slider("Quantos vestibulares exibir:", min_value=3, max_value=len(df_vestibulares), value=len(df_vestibulares))

top_vest = df_vestibulares.sort_values("buscas", ascending=False).head(top_n_vest)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=top_vest, x="buscas", y="vestibular", palette="coolwarm", ax=ax, orient="h")
ax.set_title("Vestibulares mais buscados")
ax.set_xlabel("Quantidade de buscas")
ax.set_ylabel("Vestibular")
st.pyplot(fig)

st.divider()

st.subheader("Detalhes")

audio_path = Path("Popularity_Voice.mp3")

with open(audio_path, "rb") as f:
    audio_bytes = f.read()

st.audio(audio_bytes, format="audio/mp3")

st.text("Usamos essa dashboard para monitorar a popularidade dos nossos serviços apresentados. Neste cenário, temos 3 painéis/visualizações. Onde a primeira visualização se remete a cursos mais buscados, ajudando o usuário a entender quais são as tendências daquele ano. ")
st.text("Já as duas visualizações restantes são direcionadas para as instituições parceiras, assim elas entenderão qual é a popularidade da sua instituição e vestibular podendo tomar uma medida caso necessário. ")

st.write("Esses dados são coletados a partir do monitoramento dos **cliques** dos usuários nas páginas e também através da **barra de pesquisa**, eles são diretamente enviados para nosso banco de dados e transformados em um dashboard com um relatório final.")
