from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Python REST API"}

@app.get("/health")
def health_check():
    return {"status": "UP"}

@app.post("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}
