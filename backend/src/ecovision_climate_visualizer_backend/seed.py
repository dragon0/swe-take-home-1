import json
import datetime as dt
from dotenv import load_dotenv
import os
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from .dal.helpers import get_engine, create_tables
from .dal.models import Location, Metric, ClimateData

def init_db(db_url:str):
    engine = get_engine(db_url)
    create_tables(engine)
    return engine

def seed(engine: Engine, seed_filename: str):
    with open(seed_filename) as f:
        seed_data = json.load(f)

    locations = seed_data.get('locations', [])
    metrics = seed_data.get('metrics', [])
    climate_data = seed_data.get('climate_data', [])

    with Session(engine) as session:
        objects = []

        for location in locations:
            objects.append(Location(**location))

        for metric in metrics:
            objects.append(Metric(**metric))

        for data_point in climate_data:
            data_point['date'] = dt.date.fromisoformat(data_point['date'])
            objects.append(ClimateData(**data_point))

        session.add_all(objects)
        session.commit()

def main():
    load_dotenv()
    db_url = os.environ.get("DB_URL", "sqlite:///database.db")
    print(f"Initializing database at {db_url}")
    engine = init_db(db_url)
    print(f"Seeding database at {db_url}")
    seed(engine, '../data/sample_data.json')

if __name__ == '__main__':
    main()

