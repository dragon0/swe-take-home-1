import datetime as dt
import enum
from sqlalchemy import ForeignKey, String, Double, Date, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Location(Base):
    __tablename__ = 'locations'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(50))
    latitude: Mapped[float] = mapped_column(Double())
    longitude: Mapped[float] = mapped_column(Double())
    region: Mapped[str] = mapped_column(String(50))

class Metric(Base):
    __tablename__ = 'metrics'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    display_name: Mapped[str] = mapped_column(String(50))
    unit: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(50))

class Quality(enum.Enum):
    excellent = 1
    good = 2
    questionable = 3
    poor = 4

class ClimateData(Base):
    __tablename__ = 'climate_data'
    id: Mapped[int] = mapped_column(primary_key=True)
    location_id: Mapped[int] = mapped_column(ForeignKey('locations.id'))
    location: Mapped[Location] = relationship()
    metric_id: Mapped[int] = mapped_column(ForeignKey('metrics.id'))
    metric: Mapped[Metric] = relationship()
    date: Mapped[dt.date] = mapped_column(Date())
    value: Mapped[float] = mapped_column(Double())
    quality: Mapped[Quality] = mapped_column(Enum(Quality))

