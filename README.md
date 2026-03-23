# 📊 Sales Forecasting using ARIMA

## 📌 Project Overview
This project aims to forecast future sales using time series analysis.  
We use historical sales data and apply the ARIMA model to predict future values.

---

## 🎯 Objective
- Analyze sales trends
- Make data stationary
- Build a forecasting model
- Predict future sales

---

## 📂 Project Structure
sales-forecasting-project/
│
├── data/
│   └── sales.csv
│
├── notebooks/
│   └── sales_forecasting.ipynb
│
├── README.md
└── requirements.txt

---

## ⚙️ Technologies Used
- Python
- Pandas
- Matplotlib
- Statsmodels

---

## 🔍 Steps Performed

### 1. Data Loading
- Loaded dataset using Pandas

### 2. Data Preprocessing
- Converted date column to datetime
- Set date as index

### 3. Exploratory Data Analysis (EDA)
- Visualized sales trend
- Used moving averages

### 4. Stationarity Check
- Applied ADF Test
- Found data non-stationary

### 5. Differencing
- Applied first-order differencing
- Made data stationary

### 6. Model Building
- Used ARIMA (1,1,1)

### 7. Forecasting
- Predicted future sales for next 5 days

---

## 📊 Results
- Sales show an increasing trend
- Forecast predicts continued growth

---

## ⚠️ Limitations
- Small dataset
- Model accuracy may be limited

---

## 🚀 Future Improvements
- Use larger dataset
- Add accuracy metrics (RMSE)
- Tune ARIMA parameters

---

## 👨‍💻 Author
**Uttam Saini**
