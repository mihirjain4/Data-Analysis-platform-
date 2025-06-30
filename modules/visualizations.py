import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def app():
    df = st.session_state.get("df")
    if df is None:
        st.warning("No dataset found. Please upload a dataset first.")
        return

    st.markdown("### 📈 Visualize Your Data")

    plot_type = st.selectbox("Select Plot Type", ["Histogram", "Box Plot", "Scatter Plot", "Pie Chart", "Correlation Heatmap"])

    if plot_type == "Histogram":
        column = st.selectbox("Select column for histogram", df.select_dtypes(include='number').columns)
        bins = st.slider("Number of bins", 5, 100, 30)
        fig = px.histogram(df, x=column, nbins=bins, title=f"Histogram of {column}")
        st.plotly_chart(fig)

    elif plot_type == "Box Plot":
        column = st.selectbox("Select column for box plot", df.select_dtypes(include='number').columns)
        fig = px.box(df, y=column, title=f"Box Plot of {column}")
        st.plotly_chart(fig)

    elif plot_type == "Scatter Plot":
        x_axis = st.selectbox("X-axis", df.select_dtypes(include='number').columns, key="scatter_x")
        y_axis = st.selectbox("Y-axis", df.select_dtypes(include='number').columns, key="scatter_y")
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter Plot: {x_axis} vs {y_axis}")
        st.plotly_chart(fig)

    elif plot_type == "Pie Chart":
        col = st.selectbox("Select column for pie chart", df.select_dtypes(include='object').columns)
        pie_data = df[col].value_counts().reset_index()
        pie_data.columns = [col, 'Count']
        fig = px.pie(pie_data, names=col, values='Count', title=f"Pie Chart of {col}")
        st.plotly_chart(fig)

    elif plot_type == "Correlation Heatmap":
        st.write("Correlation Matrix:")
        corr = df.select_dtypes(include='number').corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        st.pyplot(fig)
