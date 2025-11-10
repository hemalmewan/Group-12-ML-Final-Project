from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load trained pipeline model
model = pickle.load(open("../best_model/best_adaboost_model.pkl", "rb"))

# App initialization
app = FastAPI()

# Input Schema
class DeliveryInput(BaseModel):
    brand: str
    assembly: str
    product_category: str
    payment_method: str
    payment_timing: str
    product_subcategory: str

@app.post("/predict")
def predict_delivery_status(data: DeliveryInput):

    # Convert input to 2D format expected by model
    input_data = [[
        data.brand,
        data.assembly,
        data.product_category,
        data.payment_method,
        data.payment_timing,
        data.product_subcategory
    ]]

    # Prediction
    prediction = model.predict(input_data)[0]

    return {"delivery_status_prediction": prediction}