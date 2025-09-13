import streamlit as st


def index():
    st.title("BuscaVest Analytics")

pages = [
    st.Page(index, title="Início"),
    st.Page("popularity.py", title="Popularidade"),
    st.Page("errors.py", title="Erros"),
    st.Page("uptime.py", title="Uptime"),
    st.Page("projection.py", title="Projeção"),
    st.Page("feedback.py", title="Alinhamento"),
]

pg = st.navigation(pages)
pg.run()
