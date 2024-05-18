from fastapi import FastAPI
from .routers import tracking

app = FastAPI()

app.include_router(tracking.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the FedEx tracking app"}
