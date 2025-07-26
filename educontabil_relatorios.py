import streamlit as st
import pandas as pd

def main():
    st.subheader("Relatórios Contábeis")
    empresas = pd.read_csv("empresas.csv")

    if empresas.empty:
        st.warning("Cadastre uma empresa primeiro.")
        return

    empresa_nome = st.selectbox("Empresa", empresas["nome"])
    empresa_id = empresas[empresas["nome"] == empresa_nome]["id"].values[0]
    lancamentos = pd.read_csv("lancamentos.csv")
    dados = lancamentos[lancamentos["empresa_id"] == empresa_id]

    if dados.empty:
        st.info("Nenhum lançamento encontrado.")
    else:
        st.write("Lançamentos encontrados:")
        st.dataframe(dados)
