from pydantic import BaseModel

class DeliveryInput(BaseModel):
    '''
    Input model for predicting delivery status.
    '''
    brand:str
    assembly_service_requested:str
    product_category:str
    payment_method:str
    payment_timing:str
    product_subcategory:str
    product_price:float
    shipping_cost:float
    assembly_cost:float
    delivery_time_days:float
    customer_rating:float

