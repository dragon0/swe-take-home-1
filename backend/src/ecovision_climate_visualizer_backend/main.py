from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from .server.v1 import router as v1_router
from .dal.helpers import get_engine, create_tables
from .seed import seed

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
    db_url = os.environ.get("DB_URL", "sqlite:///database.db")
    engine = get_engine(db_url)
    create_tables(engine)

    should_db_seed = os.environ.get("DB_SEED")
    if should_db_seed:
        seed(engine, '../data/sample_data.json')
        

@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(v1_router, prefix="/api/v1")

