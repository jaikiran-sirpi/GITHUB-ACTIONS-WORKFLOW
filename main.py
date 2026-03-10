from fastapi import FastAPI
from datetime import datetime
import socket
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI application running inside Docker",
        "hostname": socket.gethostname(),
        "time": str(datetime.now())
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/user/{name}")
def get_user(name: str):
    return {
        "user": name,
        "message": f"Hello {name}, welcome to the FastAPI Docker app"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
