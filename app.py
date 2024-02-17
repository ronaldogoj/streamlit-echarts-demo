
import time

import streamlit as st

import pandas as pd


def main():
    st.title("Streamlit ECharts Demo Ronaldo")



    # Menu lateral
    with st.sidebar:

        st.sidebar.header("Configurações")
        num_apartamentos = st.sidebar.number_input("Número de Apartamentos", min_value=1, value=84, step=1)
        cota_minima_individual = st.sidebar.number_input("Cota Mínima Individual", min_value=1, value=15, step=1)
        tra = st.sidebar.number_input("TRA", min_value=0.0, value=5.0506, step=0.0001)
        multiplicador = st.sidebar.number_input("Multiplicador", min_value=1, value=10, step=1)
        valor_esgoto_percent = st.sidebar.number_input("Valor Esgoto (%)", min_value=0, max_value=100, value=100, step=1)

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])

    if uploaded_file is not None:
        st.subheader("File Content:")
        file_extension = uploaded_file.name.split(".")[-1]

        # Check file type and read accordingly
        if file_extension.lower() == "csv":
            df = pd.read_csv(uploaded_file)
        elif file_extension.lower() in ["txt", "log"]:
            df = pd.read_table(uploaded_file, sep='\t')
        elif file_extension.lower() in ["xls", "xlsx"]:
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        else:
            st.error(f"Unsupported file type: {file_extension}")
            return

        # Display the DataFrame
        st.write(df)

        time.sleep(20)

        # Show result in a popup
        st.success("File uploaded successfully!")



if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
    )
    main()

