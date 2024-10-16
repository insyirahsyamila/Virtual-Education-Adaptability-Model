import pickle
import os

model_path = 'model.pkl'

if not os.path.exists(model_path):
    print(f"Error: '{model_path}' does not exist in the current directory.")
    exit(1)

try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("model.pkl loaded successfully.")
except Exception as e:
    print(f"Failed to load 'model.pkl': {e}")
