#!/usr/bin/env python
# coding: utf-8

#Import libraries
import pickle
from flask import Flask, request, jsonify


#Parameters
model_file = 'model_C=1.0.bin'


# Load the model
print("Importing model")
with open(model_file,'rb') as f_in:
    dv,model = pickle.load(f_in)

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

    
##Notes
#To run flask app use the command
#python your-script.py

#This will give a warning that running this way is not recommended in production and to use a production WSGI (like gunicorn)
#To run a service in production 
#1. install gunicorn
#pip install gunicorn
#
#2. Run gunicorn as (assuming you want to listen on 0.0.0.0 on port 9696, your script name is 'your-script.py' and the instance flask app is defined as 'app')
#gunicorn --bind=0.0.0.0:996 your-script:app