from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from .server.v1 import router as v1_router

app = FastAPI(title="EcoVision API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    load_dotenv()
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(v1_router, prefix="/api/v1")

