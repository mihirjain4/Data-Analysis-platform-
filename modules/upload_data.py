import streamlit as st
import pandas as pd

def app():
    st.info("Upload a CSV or Excel file to get started.")

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
    dataset_name = st.text_input("Enter a name for your dataset")

    if uploaded_file is not None and dataset_name:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file type.")
                return

            st.session_state.df = df
            st.success(f"'{dataset_name}' uploaded successfully! ({df.shape[0]} rows × {df.shape[1]} columns)")
            st.session_state.step = 2

            with st.expander("Preview Data"):
                st.dataframe(df.head())

        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.warning("Please upload a file and name your dataset to proceed.")
