import streamlit as st
import pandas as pd

def main():
    st.subheader("Indicadores Financeiros")
    lancamentos = pd.read_csv("lancamentos.csv")

    if lancamentos.empty:
        st.info("Nenhum lançamento registrado.")
        return

    total_receitas = lancamentos[lancamentos["credito"] == "Receita"]["valor"].sum()
    total_despesas = lancamentos[lancamentos["debito"] == "Despesa"]["valor"].sum()

    st.metric("💰 Total de Receitas", f"R$ {total_receitas:,.2f}")
    st.metric("💸 Total de Despesas", f"R$ {total_despesas:,.2f}")
    st.metric("📊 Resultado do Período", f"R$ {total_receitas - total_despesas:,.2f}")
