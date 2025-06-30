import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    df = st.session_state.get("df")
    if df is None:
        st.warning("No dataset found. Please upload a dataset first.")
        return

    st.markdown("### 🤖 Model Training & Evaluation")

    # Select target column
    target_column = st.selectbox("Select Target Column", df.columns)

    # Model selection
    model_choice = st.selectbox("Choose a Model", ["Logistic Regression", "Random Forest", "SVM"])

    # Train-test split
    test_size = st.slider("Test Set Size (%)", 10, 50, 20)
    random_state = st.number_input("Random State", value=42)

    if st.button("🚀 Train Model"):
        try:
            X = df.drop(columns=[target_column])
            y = df[target_column]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size / 100, random_state=random_state
            )

            if model_choice == "Logistic Regression":
                model = LogisticRegression(max_iter=1000)
            elif model_choice == "Random Forest":
                model = RandomForestClassifier()
            else:
                model = SVC()

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            st.session_state.model = model
            st.success("✅ Model trained successfully!")

            st.subheader("📈 Classification Report")
            st.text(classification_report(y_test, y_pred))

            st.subheader("📉 Confusion Matrix")
            fig, ax = plt.subplots()
            sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', ax=ax)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error training model: {e}")
