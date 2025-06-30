import streamlit as st
import sweetviz as sv
import os

def app():
    df = st.session_state.get("df")
    if df is None:
        st.warning("No dataset found. Please upload a dataset first.")
        return

    st.markdown("### 📊 Automated EDA Report")

    if st.button("🧪 Generate EDA Report"):
        report = sv.analyze(df)
        report_path = "eda_report.html"
        report.show_html(filepath=report_path, open_browser=False)
        st.session_state.eda_ready = True
        st.success("EDA report generated!")

    if st.session_state.get("eda_ready"):
        with st.expander("🔗 View EDA Report"):
            st.components.v1.html(open("eda_report.html", "r").read(), height=600, scrolling=True)

        with open("eda_report.html", "rb") as f:
            st.download_button("⬇️ Download Report", f, file_name="EDA_Report.html")