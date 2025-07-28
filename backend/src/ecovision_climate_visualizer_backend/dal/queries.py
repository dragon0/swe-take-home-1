from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Location, Metric, ClimateData

def get_all_climate_data(session: Session):
    stmt = select(ClimateData).join(ClimateData.location).join(ClimateData.metric)
    climate_data = session.scalars(stmt).all()
    return climate_data

def get_all_locations(session: Session):
    return session.query(Location).all()

def get_all_metrics(session: Session):
    return session.query(Metric).all()

