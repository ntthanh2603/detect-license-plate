from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Driver(Base):
    __tablename__ = "driver"

    cid = Column(Integer, primary_key=True)
    name = Column(String(35))
    money = Column(Integer,default=0)
    password = Column(String(35), nullable=False)

class LicensePlate(Base):
    __tablename__ = "license_plate"

    license_plate = Column(String(35), primary_key=True)
    cid = Column(Integer, ForeignKey("driver.cid"), nullable=False)
    vehicle_parameters = Column(String(255), nullable=False)

class TransactionHistory(Base):
    __tablename__ = "transaction_history"

    th_id = Column(Integer, primary_key=True)
    license_plate_id = Column(String(35), ForeignKey("license_plate.license_plate"), nullable=False)
    station_id = Column(Integer, ForeignKey("road_toll_plaza.station_id"), nullable=False)
    time = Column(DateTime, nullable=False)
    money = Column(Integer, default=0)

class RoadTollPlaza(Base):
    __tablename__ = "road_toll_plaza"

    station_id = Column(Integer, primary_key=True)
    name_station = Column(String(35), nullable=False)
    location = Column(String(255), nullable=False)
    password_station = Column(String(35), nullable=False)