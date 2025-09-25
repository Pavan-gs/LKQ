from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Render web form

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    data = {
        'age': float(request.form['age']),
        'purchase_history': float(request.form['purchase_history']),
        'price': float(request.form['price']),
        'discount': float(request.form['discount']),
        'stock_level': float(request.form['stock_level'])
    }
    df_input = pd.DataFrame([data])
    prediction = model.predict(df_input)[0]
    prob = model.predict_proba(df_input)[0][1]
    # Log prediction
    with open('predictions.log', 'a') as f:
        f.write(f"Input: {data}, Prediction: {prediction}, Prob: {prob}\n")
    return render_template('index.html', prediction=prediction, probability=prob)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)