from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: str
    total_amount: float

class OrderResponse(BaseModel):
    order_id: str
    status: str
    total_amount: float
