import streamlit as st
import pandas as pd
import os

def main():
    st.subheader("Cadastro de Empresa")

    nome = st.text_input("Nome da empresa")
    cnpj = st.text_input("CNPJ")
    responsavel = st.text_input("Responsável")

    if st.button("Cadastrar"):
        df = pd.read_csv("empresas.csv")
        novo_id = len(df) + 1
        df.loc[len(df)] = [novo_id, nome, cnpj, responsavel]
        df.to_csv("empresas.csv", index=False)
        st.success("Empresa cadastrada com sucesso!")
