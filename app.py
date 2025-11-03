from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "ML Model API is running!"

@app.route('/predict', methods=['GET'])
def predict():
    # In a real app, you'd load a model and process input data.
    # Here, we just return a static prediction.
    prediction = {
        "customer_id": 123,
        "will_churn": True,
        "probability": 0.85
    }
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)