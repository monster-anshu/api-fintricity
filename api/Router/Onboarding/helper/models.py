from sqlalchemy import Boolean, Column, Date, DateTime,Numeric,Text , MetaData, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Countries(Base):
    __tablename__ = 'countries'
    country_code = Column(Text, primary_key = True)
    country_name = Column(Text)
    country_currency = Column(Text)
    is_active = Column(Boolean)
    created_by = Column(Text)
    updated_by = Column(Text)
    created_date = Column(Date)
    updated_date = Column(Date)
    __table_args__ = {'schema': 'kendra_sustain'}

class States(Base):
    __tablename__ = 'state'
    state_id = Column(Numeric, primary_key = True)
    country_code = Column(Text)
    state_name = Column(Text)
    state_code = Column(Text)
    is_active = Column(Boolean)
    created_by = Column(Text)
    updated_by = Column(Text)
    created_date = Column(DateTime)
    updated_date = Column(DateTime)
    __table_args__ = {'schema': 'kendra_sustain'}

class City(Base):
    __tablename__ = 'city'
    city_id = Column(Numeric , primary_key = True)
    state_id = Column(Numeric)
    city_name = Column(Text)
    city_code = Column(Text)
    is_active = Column(Boolean)
    created_by = Column(Text)
    updated_by = Column(Text)
    created_date = Column(DateTime)
    updated_date = Column(DateTime)
    __table_args__ = {'schema': 'kendra_sustain'}


