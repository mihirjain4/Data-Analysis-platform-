import streamlit as st
import pandas as pd
from io import BytesIO

def app():
    df = st.session_state.get("df")
    model = st.session_state.get("model")

    if df is None:
        st.warning("No dataset found.")
        return

    st.markdown("### 📄 Download Final Report")

    buffer = BytesIO()

    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        # Save cleaned dataset
        df.to_excel(writer, index=False, sheet_name='Cleaned_Data')

        # Optionally save model info
        if model:
            model_info = pd.DataFrame({
                "Model Type": [type(model).__name__],
                "Parameters": [str(model.get_params())]
            })
            model_info.to_excel(writer, index=False, sheet_name='Model_Info')

        writer.save()
        st.success("✅ Report compiled successfully!")

    st.download_button(
        label="⬇️ Download Report as Excel",
        data=buffer,
        file_name="data_analytics_report.xlsx",
        mime="application/vnd.ms-excel"
    )
