import streamlit as st
import pandas as pd
import numpy as np
import random

st.set_page_config(page_title="Dashboard 2 - Taxa de Erro em Requisições")

# ========= MOCK DATA =========
np.random.seed(42)

# Contextos possíveis
contextos = ["Autenticação", "Catálogo", "Exercícios", "Trilhas", "Usuários", "Pagamentos"]

# Status codes + labels
status_codes = {
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    409: "Conflict",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable"
}

# Função para gerar bodies mock
def gerar_request_body():
    return {
        "user_id": random.randint(1000, 2000),
        "action": random.choice(["login", "buscar_curso", "enviar_exercicio", "acessar_trilha"]),
        "payload": {"data": random.randint(1, 100)}
    }

# Criando dataset mock de 100 requisições com erro
df_erros = pd.DataFrame({
    "contexto": np.random.choice(contextos, 100),
    "status_code": np.random.choice(list(status_codes.keys()), 100),
    "request_body": [gerar_request_body() for _ in range(100)]
})

# Label para status
df_erros["status_label"] = df_erros["status_code"].map(status_codes)

# ========= DASHBOARD =========
st.title("🚨 Taxa de Erro em Requisições")

tab1, tab2 = st.tabs(["Por Contexto do Erro", "Por Status Code"])

# --- 1. Agrupamento por contexto ---
with tab1:
    st.subheader("📂 Erros agrupados por contexto")

    agrupado_ctx = df_erros.groupby("contexto").size().reset_index(name="qtd").sort_values("qtd", ascending=False)

    for _, row in agrupado_ctx.iterrows():
        contexto = row["contexto"]
        qtd = row["qtd"]

        with st.expander(f"{contexto} — {qtd} erros"):
            subset = df_erros[df_erros["contexto"] == contexto].head(50)
            for i, req in subset.iterrows():
                with st.expander(f"❌ Status {req['status_code']} {req['status_label']} — Req {i}"):
                    st.json(req["request_body"])

# --- 2. Agrupamento por status code ---
with tab2:
    st.subheader("⚡ Erros agrupados por Status Code")

    agrupado_status = df_erros.groupby(["status_code", "status_label"]).size().reset_index(name="qtd")
    agrupado_status = agrupado_status.sort_values("qtd", ascending=False)

    for _, row in agrupado_status.iterrows():
        status_code = row["status_code"]
        status_label = row["status_label"]
        qtd = row["qtd"]

        with st.expander(f"{status_code} {status_label} — {qtd} erros"):
            subset = df_erros[df_erros["status_code"] == status_code].head(50)
            for i, req in subset.iterrows():
                with st.expander(f"📄 Contexto {req['contexto']} — Req {i}"):
                    st.json(req["request_body"])

st.divider()
st.subheader("Detalhes")
st.text("\nEsta visualização tem como público alvo o time de operações, o qual, com a utilização da mesma, poderá fazer observações/análises precisas sobre erros ou requisições suspeitas às mais diversas rotas do nosso website.")