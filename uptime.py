import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Uptime e Desempenho")

st.title("🖥️ Uptime e Desempenho de Servidores")

# ================= Parte 1: Status Atual =================
st.header("1. Status Atual dos Microserviços")

microservicos = [
    "Core API",
    "Trilhas API",
    "Web Analytics",
    "Data Pipelines",
    "DB sa-east-1a",
    "DB sa-east-1b",
    "Web Core",
    "Web Trilhas",
    "Autenticação",
    "Parceirias",
]
status = ["online"] * 10
status[3] = "offline"  # um microserviço offline proposital

# Grid simples com checkmark/X
cols = st.columns(5)
for i, ms in enumerate(microservicos):
    col = cols[i % 5]
    if status[i] == "online":
        col.markdown(f"✅ **{ms}**")
    else:
        col.markdown(f"❌ **{ms}**")

# ================= Parte 2: Histórico de Downtime =================
st.header("2. Histórico de Downtime")

# Função para gerar datas aleatórias
def gerar_datas(start_year=2023, end_year=2025, n=10):
    datas = []
    for _ in range(n):
        ano = random.randint(start_year, end_year)
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)
        hora = random.randint(0, 23)
        minuto = random.randint(0, 59)
        datas.append(datetime(ano, mes, dia, hora, minuto))
    return sorted(datas)

downtime_events = gerar_datas(15)
causas = [
    "Atualização crítica do servidor",
    "Falha de rede",
    "Excesso de carga",
    "Erro de configuração",
    "Problema de hardware"
]
repercussoes = [
    "Usuários não conseguiram acessar o serviço por 30 min",
    "Alguns módulos ficaram indisponíveis",
    "Falha parcial, perda de dados mínima",
    "Serviço totalmente offline por 1h",
    "Interrupção temporária dos backups"
]

for i, dt in enumerate(downtime_events):
    with st.expander(f"Falha em {dt.strftime('%d/%m/%Y %H:%M')}"):
        st.markdown(f"**Serviço afetado:** {random.choice(microservicos)}")
        st.markdown(f"**Causa:** {random.choice(causas)}")
        st.markdown(f"**Repercussão:** {random.choice(repercussoes)}")

st.divider()

st.subheader("Detalhes")

st.text("Usamos essa dashboard para monitorar a saúde de nossos serviços. Neste cenário, temos 10 implantações diferentes. Qualquer turbulência nas operações é catalogada e adicionada ao histórico de downtimes. Isso é útil para o time de operações para identificar que serviço pode estar causando falhas na interface do usuário e identificar problemas recorrentes")

st.write("Os dados dessa visualização são atulizados a cada minuto. Cada serviço possui um endpoint `/health`, que retorna um simples status 200 para sucesso, garantindo que tudo está em ordem")

st.text('Isso é similar ao que outras plataformas de tecnologia oferecem de forma aberta para seus usuários, como o GitHub:')

st.image("./githubstatus.png")
