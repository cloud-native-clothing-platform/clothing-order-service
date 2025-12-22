from fastapi import APIRouter
from src.models.schemas import OrderCreate, OrderResponse
from src.services.order_service import OrderService

router = APIRouter()

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate):
    return OrderService.create_order(order)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: str):
    return OrderService.get_order(order_id)
