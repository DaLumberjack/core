"""This file contains the database models for Communifarm."""

from sqlalchemy import Column, DateTime, Float, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SensorRecord(Base):
    """A table for storing historical records of sensor data."""

    __tablename__ = "cf_sensor_record"
    # pk auto updated by sql
    id = Column(Integer, primary_key=True)
    field_id = Column(String, index=True, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    entity_id = Column(String, nullable=False, index=True)
    value = Column(Float, nullable=False)


class SeedInventoryRecord(Base):
    """Stores and maintains all seeds that have been added to this instance of CF."""

    __tablename__ = "cf_seed_inventory"
    # pk auto updated by sql
    id = Column(Integer, primary_key=True)
    field_id = Column(String, index=True, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    seed_record_id = Column(String, nullable=False, index=True)
    seller = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    price_field = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    quantity_field = Column(String, nullable=False)


class SeedRecord(Base):
    """Stores and maintains all seeds the are available to Communifarm."""

    __tablename__ = "cf_seed_inventory"
    # pk auto updated by sql
    id = Column(Integer, primary_key=True)
    field_id = Column(String, index=True, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    seed_id = Column(String, nullable=False, index=True)
    scientific_name = Column(String, nullable=False)
