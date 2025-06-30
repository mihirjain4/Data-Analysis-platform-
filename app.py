import streamlit as st
from modules import upload_data, data_overview, eda_report, data_cleaning, visualizations, feature_engineering, model_training, export_model, download_report

st.set_page_config(page_title="Data Analytics Platform", layout="wide")
st.title("📊 All-in-One Data Analytics Platform")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "df" not in st.session_state:
    st.session_state.df = None

# Step 1: Upload CSV
if st.session_state.step == 1:
    st.subheader("Step 1: Upload Your Dataset")
    upload_data.app()

# Step 2: Data Overview
if st.session_state.step >= 2 and st.session_state.df is not None:
    st.subheader("Step 2: Data Overview")
    data_overview.app()
    if st.button("➡️ Proceed to EDA Report"):
        st.session_state.step = 3

# Step 3: EDA Report
if st.session_state.step >= 3:
    st.subheader("Step 3: Exploratory Data Analysis")
    eda_report.app()
    if st.button("➡️ Proceed to Data Cleaning"):
        st.session_state.step = 4

# Step 4: Data Cleaning
if st.session_state.step >= 4:
    st.subheader("Step 4: Data Cleaning")
    data_cleaning.app()
    if st.button("➡️ Proceed to Visualization"):
        st.session_state.step = 5

# Step 5: Visualizations
if st.session_state.step >= 5:
    st.subheader("Step 5: Data Visualization")
    visualizations.app()
    if st.button("➡️ Proceed to Feature Engineering"):
        st.session_state.step = 6

# Step 6: Feature Engineering
if st.session_state.step >= 6:
    st.subheader("Step 6: Feature Engineering")
    feature_engineering.app()
    if st.button("➡️ Proceed to Model Training"):
        st.session_state.step = 7

# Step 7: Model Training
if st.session_state.step >= 7:
    st.subheader("Step 7: Model Training & Evaluation")
    model_training.app()
    if st.button("➡️ Proceed to Export Model"):
        st.session_state.step = 8

# Step 8: Export Model
if st.session_state.step >= 8:
    st.subheader("Step 8: Export Trained Model")
    export_model.app()
    if st.button("➡️ Proceed to Download Report"):
        st.session_state.step = 9

# Step 9: Download Report
if st.session_state.step >= 9:
    st.subheader("Step 9: Download Analysis Report")
    download_report.app()
