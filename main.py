from fastapi import FastAPI, HTTPException

app = FastAPI(title="DaaS Benchmark", version="1.0.0")

def calculate_discount(price: float, discount_percent: float) -> float:
    if price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid price or discount")
    return round(price * (1 - discount_percent / 100), 2)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/discount")
def get_discount(price: float, discount: float):
    try:
        final_price = calculate_discount(price, discount)
        return {"original_price": price, "final_price": final_price}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))