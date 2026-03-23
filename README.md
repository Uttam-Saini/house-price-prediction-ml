🏠 House Price Prediction System (Machine Learning Project)

📌 Overview

This project is a Machine Learning-based system that predicts house prices using various features such as number of rooms, area, and other housing attributes. The model is built using Linear Regression and trained on a real-world dataset.

⸻

🎯 Objective

To build an end-to-end Machine Learning pipeline that:
	•	Understands housing data
	•	Performs data cleaning and analysis
	•	Trains a regression model
	•	Evaluates model performance
	•	Predicts house prices for new data

⸻

🛠 Tech Stack
	•	Python
	•	Pandas
	•	NumPy
	•	Matplotlib
	•	Seaborn
	•	Scikit-learn
	•	Jupyter Notebook
  
📂 Project Structure
house-price-prediction/
│
├── data/
│   └── housing.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   └── predict.py
│
├── models/
│   └── house_model.pkl
│
└── README.md

⚙️ Workflow

1. Data Collection
	•	Used Boston Housing dataset
	•	Contains features like crime rate, number of rooms, tax, etc.

2. Data Cleaning
	•	Checked for missing values
	•	Removed duplicates
	•	Ensured dataset consistency

3. Exploratory Data Analysis (EDA)
	•	Used correlation heatmap to understand relationships
	•	Identified important features affecting house prices
	•	Found strong correlation between rm (rooms) and price

4. Feature Selection
	•	Features (X): All columns except medv
	•	Target (y): medv (house price)

5. Train-Test Split
	•	Split dataset into:
	•	80% training data
	•	20% testing data

6. Model Training
	•	Used Linear Regression model from Scikit-learn
	•	Model learns relationship between features and target

7. Model Evaluation
	•	MAE (Mean Absolute Error): ~3.18
	•	R² Score: ~0.66

8. Prediction
	•	Predicted house prices using trained model
	•	Created a separate script for predictions

9. Model Saving
	•	Saved trained model using Pickle (.pkl file)

🧠 Key Learnings
	•	Understanding of Machine Learning workflow
	•	Difference between features and target variable
	•	Importance of data cleaning and EDA
	•	Model evaluation using MAE and R²
	•	Saving and loading models using Pickle
	•	Creating reusable prediction scripts

⸻

🚀 Future Improvements
	•	Try advanced models (Random Forest, XGBoost)
	•	Hyperparameter tuning
	•	Deploy as a web application (Flask/Django)
	•	Add user interface for input

⸻

👨‍💻 Author

Uttam Saini

⸻

⭐ If you like this project

Give it a ⭐ on GitHub!
