from fastapi import FastAPI
import requests

app = FastAPI()

USER_SERVICE = "http://user-service:8000"
PRODUCT_SERVICE = "http://product-service:8000"

@app.get("/products")
def get_products():
    return requests.get(f"{PRODUCT_SERVICE}/products").json()

@app.get("/users")
def get_users():
    return requests.get(f"{USER_SERVICE}/users").json()
