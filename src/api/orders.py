from fastapi import APIRouter
from src.models.schemas import OrderCreate, OrderResponse

router = APIRouter()

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate):
    return OrderResponse(
        order_id="ORD-123",
        status="CREATED",
        total_amount=order.total_amount
    )

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: str):
    return OrderResponse(
        order_id=order_id,
        status="CREATED",
        total_amount=1999.99
    )
