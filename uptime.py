import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Uptime e Desempenho", layout="wide")

st.title("🖥️ Dashboard 5 - Uptime e Desempenho de Servidores")

# ================= Parte 1: Status Atual =================
st.header("1. Status Atual dos Microserviços")

microservicos = [f"Serviço {i}" for i in range(1, 11)]
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
