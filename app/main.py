# app/main.py
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, CI/CD"}

def main():
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000
    )


if __name__ == "__main__":
    main()