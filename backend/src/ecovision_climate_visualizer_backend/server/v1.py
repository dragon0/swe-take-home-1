# app.py - EcoVision: Climate Visualizer API

import datetime as dt
from fastapi import APIRouter, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict, List, Any, Annotated, Literal
from pydantic import BaseModel

from .db import SessionDep
from ..dal.models import Location, Metric, ClimateData
from ..dal.queries import get_filtered_climate_data, get_all_locations, get_all_metrics

router = APIRouter()

# Quality weights to be used in calculations
QUALITY_WEIGHTS = {
    'excellent': 1.0,
    'good': 0.8,
    'questionable': 0.5,
    'poor': 0.3
}

class FilterParams(BaseModel):
    location_id: int | None = None
    start_date : dt.date | None = None
    end_date : dt.date | None = None
    metric : str | None = None
    quality_threshold: Literal["poor", "questionable", "good", "excellent"] | None = None


class ClimateResponseData(BaseModel):
    id: int
    location_id: int
    location_name: str
    latitude: float
    longitude: float
    date: str
    metric: str
    value: float
    unit: str
    quality: str

class ClimateResponseMeta(BaseModel):
    total_count: int
    page: int
    per_page: int

class ClimateResponse(BaseModel):
    data: list[ClimateResponseData]
    meta: ClimateResponseMeta


@router.get('/climate')
async def get_climate_data(filter: Annotated[FilterParams, Query()], session: SessionDep) -> ClimateResponse:
    """
    Retrieve climate data with optional filtering.
    Query parameters: location_id, start_date, end_date, metric, quality_threshold

    Returns climate data in the format specified in the API docs.
    """
    # TODO: Implement this endpoint
    # 1. Get query parameters from request.args
    # 2. Validate quality_threshold if provided
    # 3. Build and execute SQL query with proper JOINs and filtering
    climate_data = get_filtered_climate_data(
            session,
            location_id=filter.location_id,
            start_date=filter.start_date,
            end_date=filter.end_date,
            metric=filter.metric,
            quality_threshold=filter.quality_threshold)

    # 4. Apply quality threshold filtering

    # 5. Format response according to API specification
    climate_data = [ClimateResponseData(
        id=data.id,
        location_id=data.location_id,
        location_name=data.location.name,
        latitude=data.location.latitude,
        longitude=data.location.longitude,
        date=data.date.isoformat(),
        metric=data.metric.name,
        value=data.value,
        unit=data.metric.unit,
        quality=data.quality.name
        ) for data in climate_data]
    # TODO Pagination not implemented yet
    climate_meta = ClimateResponseMeta(total_count=len(climate_data), page=1, per_page=50)


    return ClimateResponse(data=climate_data, meta=climate_meta)

class LocationResponseData(BaseModel):
    id: int
    name: str
    country: str
    latitude: float
    longitude: float

class LocationResponse(BaseModel):
    data: list[LocationResponseData]

@router.get('/locations')
async def get_locations(session: SessionDep) -> LocationResponse:
    """
    Retrieve all available locations.

    Returns location data in the format specified in the API docs.
    """
    # TODO: Implement this endpoint
    # 1. Query the locations table
    locations = get_all_locations(session)

    # 2. Format response according to API specification
    locations = [LocationResponseData(
        id=data.id,
        name=data.name,
        country=data.country,
        latitude=data.latitude,
        longitude=data.longitude,
        ) for data in locations]

    return LocationResponse(data=locations)

class MetricResponseData(BaseModel):
    id: int
    name: str
    display_name: str
    unit: str
    description: str

class MetricResponse(BaseModel):
    data: list[MetricResponseData]

@router.get('/metrics')
async def get_metrics(session: SessionDep) -> MetricResponse:
    """
    Retrieve all available climate metrics.

    Returns metric data in the format specified in the API docs.
    """
    # TODO: Implement this endpoint
    # 1. Query the metrics table
    metrics = get_all_metrics(session)
    # 2. Format response according to API specification
    metrics = [MetricResponseData(
        id=data.id,
        name=data.name,
        display_name=data.display_name,
        unit=data.unit,
        description=data.description
        ) for data in metrics]


    return MetricResponse(data=metrics)

@router.get('/summary')
async def get_summary():
    """
    Retrieve quality-weighted summary statistics for climate data.
    Query parameters: location_id, start_date, end_date, metric, quality_threshold
    
    Returns weighted min, max, and avg values for each metric in the format specified in the API docs.
    """
    # TODO: Implement this endpoint
    # 1. Get query parameters from request.args
    # 2. Validate quality_threshold if provided
    # 3. Get list of metrics to summarize
    # 4. For each metric:
    #    - Calculate quality-weighted statistics using QUALITY_WEIGHTS
    #    - Calculate quality distribution
    #    - Apply proper filtering
    # 5. Format response according to API specification
    
    return {"data": {}}

@router.get('/trends')
async def get_trends():
    """
    Analyze trends and patterns in climate data.
    Query parameters: location_id, start_date, end_date, metric, quality_threshold
    
    Returns trend analysis including direction, rate of change, anomalies, and seasonality.
    """
    # TODO: Implement this endpoint
    # 1. Get query parameters from request.args
    # 2. Validate quality_threshold if provided
    # 3. For each metric:
    #    - Calculate trend direction and rate of change
    #    - Identify anomalies (values > 2 standard deviations)
    #    - Detect seasonal patterns if sufficient data
    #    - Calculate confidence scores
    # 4. Format response according to API specification
    
    return {"data": {}}

