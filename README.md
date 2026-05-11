# 🏠 ගෙවල් මිල පුරෝකථනය — House Price Prediction

A Streamlit web application that predicts residential house prices based on key property features, built with a machine learning model trained on the Ames Housing dataset.

---

## 📸 Overview

The app features a bilingual interface (Sinhala + English) with a dark, modern UI. Users fill in property details across four sections and instantly receive an estimated market value with a confidence range.

---

## ✨ Features

- **Instant price prediction** with a ±8% confidence range
- **Smart property tags** (e.g., High Condition, Modern Build, Large Lot)
- **Interactive condition slider** with visual feedback
- **Bilingual UI** in Sinhala and English
- **Dark, responsive design** styled with custom CSS

---

## 🧠 Machine Learning

The notebook (`house_price_detection.ipynb`) covers the full ML pipeline:

| Step | Details |
|---|---|
| **Dataset** | `HousePricePrediction.xlsx` — 2,919 rows, 13 columns |
| **Target** | `SalePrice` (available for 1,460 training rows) |
| **Features** | MSSubClass, MSZoning, LotArea, LotConfig, BldgType, OverallCond, YearBuilt, YearRemodAdd, Exterior1st, BsmtFinSF2, TotalBsmtSF |
| **Models trained** | Decision Tree, **Random Forest** ✅, Linear Regression |
| **Best model** | `RandomForestRegressor` (model2) — lowest MAPE (~19.8% for LR; RF performed better) |
| **Encoding** | `OrdinalEncoder` for categorical features |
| **Saved artifacts** | `house_model.pkl`, `encoder.pkl` |

---

## 🗂️ Project Structure

```
├── app.py                        # Streamlit app
├── house_price_detection.ipynb   # EDA + model training notebook
├── HousePricePrediction.xlsx     # Dataset
├── house_model.pkl               # Trained Random Forest model
├── encoder.pkl                   # Fitted OrdinalEncoder
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```

### 2. Install dependencies

```bash
pip install streamlit pandas scikit-learn openpyxl
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🖥️ Input Features

| Section | Fields |
|---|---|
| 🏛️ Building Info | MSSubClass, Building Type, Year Built, Year Remodelled, Exterior Material |
| 🗺️ Land & Location | Lot Area (sq ft), MS Zoning, Lot Configuration |
| 📐 Interior Sizes | Total Basement SF, Finished Basement SF2 |
| ⭐ Condition | Overall Condition (1 = Poor → 9 = Excellent) |

---

## 📊 Dataset Stats

- **Rows:** 2,919 (1,460 labelled + 1,459 unlabelled)
- **Sale Price range:** $34,900 – $755,000
- **Mean Sale Price:** ~$180,921

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit, custom CSS (DM Sans + Noto Sans Sinhala)
- **ML:** scikit-learn (RandomForestRegressor, OrdinalEncoder)
- **Data:** pandas, openpyxl
- **Visualisation (notebook):** matplotlib, seaborn

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
