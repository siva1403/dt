from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "order", "price": 50000},
    {"id": 2, "name": "order", "price": 20000}
]

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def add_product(product: dict):
    products.append(product)
    return product
