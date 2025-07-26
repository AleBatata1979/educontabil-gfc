import streamlit as st
import pandas as pd
import educontabil_cadastro
import educontabil_lancamentos
import educontabil_relatorios
import educontabil_indicadores

st.set_page_config(page_title="EduContábil GFC", layout="wide")
st.title("📚 EduContábil GFC - Simulador Contábil Didático")

menu = st.sidebar.radio("Navegação", ["Cadastro", "Lançamentos", "Relatórios", "Indicadores"])

if menu == "Cadastro":
    educontabil_cadastro.main()
elif menu == "Lançamentos":
    educontabil_lancamentos.main()
elif menu == "Relatórios":
    educontabil_relatorios.main()
elif menu == "Indicadores":
    educontabil_indicadores.main()
