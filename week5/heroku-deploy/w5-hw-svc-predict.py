#Import libraries
import pickle
from flask import Flask, request, jsonify


#Parameters
dv_file = "dv.bin"
model_file = "model1.bin"

# Load the model
print("Importing model")
with open(model_file,'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file,'rb') as f_in:
    dv = pickle.load(f_in)

def predict_churn(customer):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = (y_pred >= 0.5)
    return y_pred, churn

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    y_pred, churn = predict_churn(customer)

    #Need to convert numpy float and boolean to python float and bool, hence use the float() and bool() as below
    result = {
            'churn_probability': float(y_pred),
            'churn': bool(churn)
            }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
