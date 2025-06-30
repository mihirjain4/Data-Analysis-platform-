# 📊 Data Analytics Platform (No-Code ML Builder)

An interactive Streamlit-based platform for complete end-to-end data analysis — from uploading data, exploring and cleaning it, visualizing patterns, engineering features, training machine learning models, and exporting reports.

---

## 🚀 Features

✅ Step-by-step workflow:
1. Upload CSV/Excel & name the dataset  
2. Data overview (shape, types, missing values)  
3. EDA report (Sweetviz-powered HTML report)  
4. Data cleaning (handle NA, remove duplicates)  
5. Visualizations (histograms, scatter, pie, heatmaps)  
6. Feature engineering (scaling, encoding)  
7. Model training (Logistic Regression, Random Forest, SVM)  
8. Export trained model as `.pkl`  
9. Download full analysis report as Excel

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Libraries:**  
  - pandas, numpy  
  - scikit-learn  
  - sweetviz  
  - seaborn, matplotlib, plotly  
  - joblib, xlsxwriter

---



## 🧑‍💻 Setup Instructions

### ✅ Create Virtual Environment

```bash
python -m venv venv
```

### ✅ Activate Environment

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### ✅ Install Requirements

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```
data_analytics_platform/
│
├── app.py                     # Main app with step-by-step logic
├── requirements.txt           # All dependencies
├── README.md
└── modules/                   # Modular features
    ├── upload_data.py
    ├── data_overview.py
    ├── eda_report.py
    ├── data_cleaning.py
    ├── visualizations.py
    ├── feature_engineering.py
    ├── model_training.py
    ├── export_model.py
    └── download_report.py
```

---

## 📌 Author

**Mihir Shah**  
Data Analyst | Data Scientist | ML Engineer  
📫 [LinkedIn](https://www.linkedin.com/in/mihir-shah-004466276)

---

