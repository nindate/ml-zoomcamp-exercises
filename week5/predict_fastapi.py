from fastapi import FastAPI
from pydantic import BaseModel
import pickle


#customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

with open('model1.bin','rb') as f_model:
    model = pickle.load(f_model)

with open('dv.bin','rb') as f_dv:
    dv = pickle.load(f_dv)


class Customer(BaseModel):
    contract: str
    tenure: int
    monthlycharges: float

app = FastAPI()

@app.get("/")
def hello():
    return {"greetings": "Welcome to learning FastAPI"}


@app.post("/predict")
def predict(customer: Customer):
    X = dv.transform(customer.dict())
    y_pred = model.predict_proba(X)[0,1]
    churn = (y_pred >= 0.5)
    result =  {"churn_probability": float(y_pred), "churn": bool(churn)}
    return result
