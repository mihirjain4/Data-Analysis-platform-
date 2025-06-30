import streamlit as st
import joblib
import os

def app():
    model = st.session_state.get("model")
    if model is None:
        st.warning("No trained model found. Please train a model first.")
        return

    st.markdown("### 💾 Export Trained Model")

    filename = st.text_input("Enter filename for model (without extension)", value="my_model")

    if st.button("💾 Save Model"):
        try:
            filepath = f"{filename}.pkl"
            joblib.dump(model, filepath)
            st.success(f"Model saved as {filepath}")

            with open(filepath, "rb") as f:
                st.download_button("⬇️ Download Saved Model", f, file_name=filepath)
        except Exception as e:
            st.error(f"Error saving model: {e}")
