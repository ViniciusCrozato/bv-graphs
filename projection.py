import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard 3 - Projeção de Crescimento")

# ========= MOCK DATA =========
np.random.seed(42)

meses = pd.date_range("2025-06-01", periods=12, freq="M").strftime("%b/%Y")

# Acessos: tendência de alta mas com quedas
acessos = [1000]
for _ in range(11):
    acessos.append(acessos[-1] + np.random.randint(-100, 400))
acessos = np.maximum(acessos, 500)  # não deixa cair abaixo de 500

# Receita: tendência de alta mas com quedas ocasionais
receita = [80_000]
for _ in range(11):
    receita.append(receita[-1] + np.random.randint(-2_000, 15_000))
receita = np.maximum(receita, 30_000)  # não deixa cair abaixo de 30k

df = pd.DataFrame({
    "mes": meses,
    "acessos": acessos,
    "receita": receita
})

# ========= PROJEÇÃO =========
# Projeção simples: último valor + média dos últimos deltas
delta_acessos = np.diff(acessos).mean()
delta_receita = np.diff(receita).mean()

proximo_mes = (pd.to_datetime(df["mes"].iloc[-1], format="%b/%Y") + pd.DateOffset(months=1)).strftime("%b/%Y")
proj_acessos = acessos[-1] + delta_acessos
proj_receita = receita[-1] + delta_receita

# ========= DASHBOARD =========
st.title("📈 Projeção de Crescimento de Receita e Usuários")

fig, ax1 = plt.subplots(figsize=(10, 6))

split_index = len(df) - 6  # Adjust this based on where your projection starts

ax1.axvspan(0, split_index, alpha=0.05, color='blue', label='Atual')
ax1.axvspan(split_index, len(df)-1, alpha=0.15, color='purple', label='Projeção')

# --- Linha de acessos (Eixo da esquerda) ---
color_acessos = "tab:blue"
ax1.set_xlabel("Mês")
ax1.set_ylabel("Acessos", color=color_acessos)
ax1.plot(df["mes"], df["acessos"], marker="o", color=color_acessos, label="Acessos")
ax1.tick_params(axis="y", labelcolor=color_acessos)

# --- Linha de receita (Eixo da direita) ---
ax2 = ax1.twinx()
color_receita = "tab:orange"
ax2.set_ylabel("Receita (R$)", color=color_receita)
ax2.plot(df["mes"], df["receita"], marker="o", color=color_receita, label="Receita")
ax2.tick_params(axis="y", labelcolor=color_receita)

# Melhorar legibilidade do eixo X
ax1.set_xticklabels(list(df["mes"]) + [proximo_mes], rotation=45)

# --- Legenda única ---
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
fig.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left", bbox_to_anchor=(0.1, 0.92))

# Título
fig.suptitle("Projeção de Crescimento - Acessos (Eixo Esquerdo) e Receita (Eixo Direito)")

st.pyplot(fig)

st.markdown(f"""
### 🔮 Projeções
- **Próximo mês ({proximo_mes})**  
  - Acessos esperados: **{int(proj_acessos)}**  
  - Receita esperada: **R$ {int(proj_receita):,}**
""")

st.divider()
st.subheader("Detalhes")
st.text("\nEsta sessão é uma medição de extrema importância para possíveis investidores, já que se trata de uma projeção de crescimento. Aqui, temos três métricas: no eixo X, que se trata do tempo em meses e no eixo Y, que se trata do fluxo de acesso (usuários) e, por fim, uma linha que representa a projeção de renda, que vai acompanhar o crescimento financeiro do projeto considerando o fluxo de acessos por mês.")