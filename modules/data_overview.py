import streamlit as st
import pandas as pd

def app():
    df = st.session_state.get("df")
    if df is None:
        st.warning("No dataset found. Please upload a dataset first.")
        return

    st.markdown("### 📋 Dataset Overview")
    st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

    with st.expander("🔍 View Columns"):
        st.write(pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isnull().sum().values
        }))

    with st.expander("📌 Preview Data"):
        st.dataframe(df.head())

    with st.expander("📉 Summary Statistics"):
        st.write(df.describe(include='all').T)

    with st.expander("⚠️ Missing Value Matrix"):
        st.write(df.isnull().sum()[df.isnull().sum() > 0])
