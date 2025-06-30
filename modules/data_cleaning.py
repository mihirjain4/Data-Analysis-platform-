import streamlit as st
import pandas as pd

def app():
    df = st.session_state.get("df")
    if df is None:
        st.warning("No dataset found. Please upload a dataset first.")
        return

    st.markdown("### 🧹 Data Cleaning Options")

    col1, col2 = st.columns(2)

    with col1:
        remove_duplicates = st.checkbox("Remove duplicate rows", value=True)
        drop_na = st.checkbox("Drop rows with missing values")
    
    with col2:
        fill_na = st.checkbox("Fill missing values")
        fill_value = st.text_input("Value to fill NA with (optional)", value="0")

    # Show before cleaning
    st.subheader("Before Cleaning:")
    st.write(f"Shape: {df.shape}")
    st.write(f"Missing values:\n{df.isnull().sum().sum()}")

    if st.button("🧼 Clean Data Now"):
        if remove_duplicates:
            df = df.drop_duplicates()
        if drop_na:
            df = df.dropna()
        if fill_na:
            df = df.fillna(value=fill_value)

        st.session_state.df = df
        st.success("Data cleaned successfully!")

        # Show after cleaning
        st.subheader("After Cleaning:")
        st.write(f"Shape: {df.shape}")
        st.write(f"Missing values:\n{df.isnull().sum().sum()}")
        st.dataframe(df.head())
