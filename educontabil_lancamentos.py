import streamlit as st
import pandas as pd
from datetime import date

def main():
    st.subheader("Lançamentos Contábeis")
    empresas = pd.read_csv("empresas.csv")

    if empresas.empty:
        st.warning("Cadastre uma empresa antes de realizar lançamentos.")
        return

    empresa_nome = st.selectbox("Empresa", empresas["nome"])
    empresa_id = empresas[empresas["nome"] == empresa_nome]["id"].values[0]
    data = st.date_input("Data", date.today())
    descricao = st.text_input("Descrição")
    debito = st.text_input("Conta Débito")
    credito = st.text_input("Conta Crédito")
    valor = st.number_input("Valor", min_value=0.0, step=0.01)

    if st.button("Registrar"):
        df = pd.read_csv("lancamentos.csv")
        novo_id = len(df) + 1
        df.loc[len(df)] = [novo_id, empresa_id, data, descricao, debito, credito, valor]
        df.to_csv("lancamentos.csv", index=False)
        st.success("Lançamento registrado com sucesso!")
