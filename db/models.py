from .database import Base
from sqlalchemy import Column, JSON, Integer, String, Float


class Ami(Base):
    __tablename__ = "ami"
    id = Column(Integer, primary_key=True, index=True)
    cust_id = Column(String)
    meter_id = Column(String)
    ratio = Column(String)
    read_time = Column(String)
    del_kwh = Column(String)
    rec_kwh = Column(String)
    del_kvarh_lag = Column(String)
