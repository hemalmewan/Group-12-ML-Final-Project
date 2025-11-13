from fastapi import FastAPI,Form,Request
from fastapi.responses import FileResponse
from delivery_status import DeliveryInput
import pickle
import pandas as pd 
from fastapi.middleware.cors import CORSMiddleware

# Load trained pipeline model
model = pickle.load(open("../best_model/best_adaboost_model.pkl", "rb"))

# App initialization
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (or specify your front-end host)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## Serve the HTML form
@app.get("/")
def serve_form():
    return FileResponse("../FrontEnd/HTML/web_site.html")  # path to your HTML file

@app.post("/predict")
def predict_delivery_status(
    price: float = Form(...),
    shipping: float = Form(...),
    assembly_cost: float = Form(...),
    delivery_days: int = Form(...),
    rating: float = Form(...),
    category: str = Form(...),
    subcategory: str = Form(...),
    brand: str = Form(...),
    assembly: str = Form(...),
    payment: str = Form(...),
    timing: str = Form(...),
    

):
    """
    Predict delivery status using trained AdaBoost model
    """

    # Convert input into DataFrame format for model
    data = pd.DataFrame([{
        "product_price": price,
        "shipping_cost": shipping,
        "assembly_cost": assembly_cost,
        "delivery_window_days": delivery_days,
        "customer_rating": rating,
        "product_category": category,
        "product_subcategory": subcategory,
        "brand": brand,
        "assembly_service_requested": assembly,
        "payment_method": payment,
        "payment_timing": timing,
        
        
    }])

    # Make prediction
    prediction = model.predict(data)[0]

    # Return result as JSON
    return {"predicted_delivery_status": prediction}


