import inspect
import textwrap
import time

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS

import pandas as pd


def main():
    st.title("Streamlit ECharts Demo Ronaldo")

    with st.sidebar:
        st.header("Configuration")
        api_options = ("echarts", "pyecharts")
        selected_api = st.selectbox(
            label="Choose your preferred API:",
            options=api_options,
        )

        page_options = (
            list(ST_PY_DEMOS.keys())
            if selected_api == "pyecharts"
            else list(ST_DEMOS.keys())
        )
        selected_page = st.selectbox(
            label="Choose an example",
            options=page_options,
        )
        demo, url = (
            ST_DEMOS[selected_page]
            if selected_api == "echarts"
            else ST_PY_DEMOS[selected_page]
        )

        if selected_api == "echarts":
            st.caption(
                """ECharts demos are extracted from https://echarts.apache.org/examples/en/index.html, 
            by copying/formattting the 'option' json object into st_echarts.
            Definitely check the echarts example page, convert the JSON specs to Python Dicts and you should get a nice viz."""
            )
        if selected_api == "pyecharts":
            st.caption(
                """Pyecharts demos are extracted from https://github.com/pyecharts/pyecharts-gallery,
            by copying the pyecharts object into st_pyecharts. 
            Pyecharts is still using ECharts 4 underneath, which is why the theming between st_echarts and st_pyecharts is different."""
            )

    #demo()
    #sourcelines, _ = inspect.getsourcelines(demo)
    #with st.expander("Source Code"):
    #    st.code(textwrap.dedent("".join(sourcelines[1:])))
    #st.markdown(f"Credit: {url}")


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

        # Create tabs for displaying DataFrames
        with st.tabs("DataFrame 1", "DataFrame 2"):
            with st.tab("DataFrame 1"):
                st.write(df)

            with st.tab("DataFrame 2"):
                # Display the same DataFrame for demonstration purposes
                # In a real application, you would load and display a different DataFrame
                st.write(df)

        # Show result in a popup
        st.success("File uploaded successfully!")



if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
    )
    main()
    with st.sidebar:
        st.markdown("---")
        st.markdown(
            '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
            unsafe_allow_html=True,
        )
