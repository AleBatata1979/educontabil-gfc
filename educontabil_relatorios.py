
import streamlit as st
import pandas as pd

def main():
    st.markdown("## 📚 EduContábil GFC - Simulador Contábil Didático")
    st.markdown("### 📄 Relatórios Contábeis")

    try:
        empresas = pd.read_csv("empresas.csv")
        lancamentos = pd.read_csv("lancamentos.csv")
    except FileNotFoundError:
        st.error("❌ Arquivos de dados não encontrados. Certifique-se de que 'empresas.csv' e 'lancamentos.csv' estejam no diretório do app.")
        return
    except pd.errors.EmptyDataError:
        st.warning("⚠️ Um dos arquivos CSV está vazio. Por favor, cadastre empresas e lançamentos.")
        return

    if empresas.empty:
        st.warning("⚠️ Nenhuma empresa cadastrada.")
        return

    empresa_nome = st.selectbox("Selecione a empresa", empresas["nome"].unique())

    if not empresa_nome:
        st.info("ℹ️ Por favor, selecione uma empresa.")
        return

    empresa_id = empresas[empresas["nome"] == empresa_nome]["id"].values[0]

    lancamentos_empresa = lancamentos[lancamentos["empresa_id"] == empresa_id]

    if lancamentos_empresa.empty:
        st.warning("⚠️ Nenhum lançamento encontrado para esta empresa.")
        return

    if st.button("🔁 Gerar Relatórios Contábeis"):

        st.subheader("📊 Balancete (Crédito vs Débito)")
        balancete = lancamentos_empresa.groupby(["debito", "credito"])["valor"].sum().reset_index()
        st.dataframe(balancete)

        st.subheader("💰 Demonstração do Resultado do Exercício (DRE)")

        receitas = lancamentos_empresa[lancamentos_empresa["credito"] == "Receita"]["valor"].sum()
        despesas = lancamentos_empresa[lancamentos_empresa["debito"] == "Despesa"]["valor"].sum()
        lucro = receitas - despesas

        dre_data = {
            "Receita Bruta": [receitas],
            "(-) Despesas": [despesas],
            "Lucro/Prejuízo": [lucro]
        }

        dre_df = pd.DataFrame(dre_data)
        st.table(dre_df.style.format("R$ {:,.2f}"))

        st.subheader("📄 Lançamentos Contábeis")
        st.dataframe(lancamentos_empresa)

        st.success("✅ Relatórios gerados com sucesso.")

if __name__ == "__main__":
    main()
