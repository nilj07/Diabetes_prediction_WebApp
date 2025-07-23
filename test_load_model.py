import pickle

   # Attempt to load the model
try:
       with open('diabetes_knn_model.pkl', 'rb') as file:
           model = pickle.load(file)
           print("Model loaded successfully:", type(model))  # Should show the model type
except Exception as e:
       print(f"Error loading model: {e}")
   