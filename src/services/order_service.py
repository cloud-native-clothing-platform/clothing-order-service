from src.models.schemas import OrderCreate, OrderResponse
import uuid


class OrderService:
    @staticmethod
    def create_order(order: OrderCreate) -> OrderResponse:
        return OrderResponse(
            order_id=f"ORD-{uuid.uuid4().hex[:8]}",
            status="CREATED",
            total_amount=order.total_amount
        )

    @staticmethod
    def get_order(order_id: str) -> OrderResponse:
        return OrderResponse(
            order_id=order_id,
            status="CREATED",
            total_amount=1999.99
        )

