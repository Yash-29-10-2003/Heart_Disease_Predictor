import joblib
import pandas as pd
from flask import Flask, request, jsonify

best_svm = joblib.load('best_svm_model.pkl')
scaler = joblib.load('scaler.pkl')
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Validating and preprocessing the input
        age = data['age']
        sex = data['sex']
        cp = data['cp']
        trestbps = data['trestbps']
        chol = data['chol']
        fbs = data['fbs']
        restecg = data['restecg']
        thalach = data['thalach']
        exang = data['exang']
        oldpeak = data['oldpeak']
        slope = data['slope']
        ca = data['ca']
        thal = data['thal']
        # Creating a user data DataFrame
        user_data = pd.DataFrame({
            'age': [age],
            'sex': [sex],
            'cp': [cp],
            'trestbps': [trestbps],
            'chol': [chol],
            'fbs': [fbs],
            'restecg': [restecg],
            'thalach': [thalach],
            'exang': [exang],
            'oldpeak': [oldpeak],
            'slope': [slope],
            'ca': [ca],
            'thal': [thal]
        })

        # Scaling the user input using the same scaler used for training
        user_data_scaled = scaler.transform(user_data)

        # Making predictions
        user_prediction = best_svm.predict(user_data_scaled)
        result = {'prediction': int(user_prediction[0])}
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()