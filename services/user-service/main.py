from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "siva", "price": 50000},
    {"id": 2, "name": "krishna", "price": 20000}
]

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def add_product(product: dict):
    products.append(product)
    return product
