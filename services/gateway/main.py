from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="API Gateway")

# Kubernetes Service URLs
USER_SERVICE = "http://user-service:8000"
PRODUCT_SERVICE = "http://product-service:8000"
ORDER_SERVICE = "http://order-service:8000"
PAYMENT_SERVICE = "http://payment-service:8000"


@app.get("/")
def home():
    return {"message": "API Gateway Running"}


# ---------------- USER SERVICE ----------------

@app.api_route("/users/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def user_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{USER_SERVICE}/{path}",
            headers=request.headers,
            content=await request.body(),
        )
    return response.json()


# ---------------- PRODUCT SERVICE ----------------

@app.api_route("/products/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def product_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{PRODUCT_SERVICE}/{path}",
            headers=request.headers,
            content=await request.body(),
        )
    return response.json()


# ---------------- ORDER SERVICE ----------------

@app.api_route("/orders/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def order_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{ORDER_SERVICE}/{path}",
            headers=request.headers,
            content=await request.body(),
        )
    return response.json()


# ---------------- PAYMENT SERVICE ----------------

@app.api_route("/payments/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def payment_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{PAYMENT_SERVICE}/{path}",
            headers=request.headers,
            content=await request.body(),
        )
    return response.json()
