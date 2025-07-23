from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained KNN model globally, only once
try:
    with open('diabetes_knn_model.pkl', 'rb') as file:
        model = pickle.load(file)
        print("Model loaded successfully:", type(model))  # Debugging line
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'The model failed to load.'}), 500
    try:
        data = request.get_json()
        print("Received data:", data)

        # Convert input data to the correct types
        features = np.array([
            int(data['pregnancies']),
            float(data['glucose']),
            float(data['blood_pressure']),
            float(data['skin_thickness']),
            float(data['insulin']),
            float(data['bmi']),
            float(data['diabetes_pedigree_function']),
            int(data['age'])
        ]).reshape(1, -1)

        # Predict
        prediction = model.predict(features)
        prediction_text = 'Likely Diabetic' if prediction[0] == 1 else 'Likely Not Diabetic'

        return jsonify({
            'prediction': prediction_text,
            'prediction_text': prediction_text
        })
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
