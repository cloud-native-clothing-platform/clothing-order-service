from fastapi import FastAPI
from src.api.orders import router as order_router

app = FastAPI(title="Clothing Order Service")

app.include_router(order_router, prefix="/orders", tags=["Orders"])

@app.get("/health")
def health_check():
    return {"status": "UP"}
