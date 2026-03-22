import pickle
import pandas as pd

# Load model
with open('../models/house_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Example input (same format as training data)
data = {
    'crim': [0.1],
    'zn': [0],
    'indus': [8],
    'chas': [0],
    'nox': [0.5],
    'rm': [6],
    'age': [60],
    'dis': [4],
    'rad': [4],
    'tax': [300],
    'ptratio': [15],
    'b': [390],
    'lstat': [10]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Predict price
prediction = model.predict(df)

print("Predicted House Price:", prediction[0])