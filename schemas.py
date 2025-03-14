from pydantic import BaseModel, Field, validator
from datetime import datetime

class Driver(BaseModel):
    cid: int = Field(..., ge=1)  # Ensure ID is greater than or equal to 1
    name: str = Field(..., max_length=35)
    money: int = Field(default=0, ge=0)  # Ensure money is non-negative
    password: str = Field(..., max_length=35)

class LicensePlate(BaseModel):
    license_plate: str = Field(..., max_length=35)
    cid_id: int = Field(...)  # Foreign key reference to Driver.cid
    vehicle_parameters: str = Field(..., max_length=255)

class TransactionHistory(BaseModel):
    th_id: int = Field(..., ge=1)  # Ensure ID is greater than or equal to 1
    license_plate_id: str = Field(..., max_length=35)  # Foreign key reference to LicensePlate.license_plate
    station_id: int = Field(...)  # Foreign key reference to RoadTollPlaza.station_id
    time: datetime = Field(...)  # Assuming datetime import
    money: int = Field(default=0, ge=0)  # Ensure money is non-negative

class RoadTollPlaza(BaseModel):
    station_id: int = Field(..., ge=1)  # Ensure ID is greater than or equal to 1
    name_station: str = Field(..., max_length=35)
    location: str = Field(..., max_length=255)
    password_station: str = Field(..., max_length=35)
