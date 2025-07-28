import datetime as dt
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Location, Metric, ClimateData, Quality

def get_all_climate_data(session: Session):
    stmt = select(ClimateData).join(ClimateData.location).join(ClimateData.metric)
    climate_data = session.scalars(stmt).all()
    return climate_data

def get_filtered_climate_data(session: Session, location_id: int | None = None, start_date: dt.date | None = None, end_date: dt.date | None = None, metric: str | None = None, quality_threshold: Quality | None = None):
    stmt = select(ClimateData).join(ClimateData.location).join(ClimateData.metric)

    if location_id:
        stmt = stmt.where(ClimateData.location_id == location_id)

    if start_date:
        stmt = stmt.where(ClimateData.date >= start_date)

    if end_date:
        stmt = stmt.where(ClimateData.date <= end_date)

    if metric:
        stmt = stmt.where(ClimateData.metric_id == metric)

    if quality_threshold:
        stmt = stmt.where(ClimateData.quality == quality_threshold)

    climate_data = session.scalars(stmt).all()
    return climate_data

def get_all_locations(session: Session):
    return session.query(Location).all()

def get_all_metrics(session: Session):
    return session.query(Metric).all()

