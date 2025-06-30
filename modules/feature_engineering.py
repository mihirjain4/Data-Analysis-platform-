import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

def app():
    df = st.session_state.get("df")
    if df is None:
        st.warning("No dataset found. Please upload a dataset first.")
        return

    st.markdown("### 🏗️ Feature Engineering")

    # Column selection
    st.subheader("Select Columns to Encode")
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    selected_cat_cols = st.multiselect("Categorical Columns", cat_cols)

    st.subheader("Select Columns to Scale")
    num_cols = df.select_dtypes(include='number').columns.tolist()
    selected_num_cols = st.multiselect("Numerical Columns", num_cols)

    scale_option = st.selectbox("Scaling Method", ["StandardScaler", "MinMaxScaler"])

    if st.button("🚀 Apply Transformations"):
        # Encode
        for col in selected_cat_cols:
            le = LabelEncoder()
            try:
                df[col] = le.fit_transform(df[col].astype(str))
            except:
                st.warning(f"Could not encode column: {col}")

        # Scale
        if scale_option == "StandardScaler":
            scaler = StandardScaler()
        else:
            scaler = MinMaxScaler()

        try:
            df[selected_num_cols] = scaler.fit_transform(df[selected_num_cols])
        except Exception as e:
            st.error(f"Error during scaling: {e}")

        st.session_state.df = df
        st.success("Transformations applied successfully!")
        st.dataframe(df.head())
