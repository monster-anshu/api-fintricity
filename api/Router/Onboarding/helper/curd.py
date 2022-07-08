from pyexpat import model
from typing import List

from sqlalchemy import true
from . import models
from sqlalchemy.orm import Session

def getAll(db:Session ):
    return db.query(models.Countries).all()

def getByISO3(db:Session,ISO3:str):
    return db.query(models.Countries).filter(models.Countries.ISO3 == ISO3).first()

def getByISO2(db:Session,ISO2:str):
    return db.query(models.Countries).filter(models.Countries.ISO2 == ISO2).first()

def getAllCountries(db:Session):
    return db.query(models.Countries).all()

def getAllStates(db:Session , country_code : str):
    return db.query(models.States).filter( models.States.country_code == country_code ).all()

def getStateByName(db:Session , state_name: str):
    return db.query(models.States).filter( models.States.state_name == state_name).all()

def getCities(db:Session , state_id : int):
    return db.query(models.City).filter(models.City.state_id == state_id).all()

def getCityByName(db:Session , city_name : str):
    print(city_name)
    return db.query(models.City).filter(models.City.city_name == city_name).all()

def add_countries(db:Session,countries : List[models.Countries]):
    country_data = []
    for country in countries:
        country_data.append (models.Countries(**country))
    db.bulk_save_objects(country_data)
    db.commit()
    return True

def add_cities(db:Session , cities : List[models.City] ):
    city_data = []
    for city in cities:
        city_data.append(models.City(**city))
    db.bulk_save_objects(city_data)
    db.commit()
    return True