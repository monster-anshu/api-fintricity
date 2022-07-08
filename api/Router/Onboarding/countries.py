from datetime import datetime
import json
import sys
from typing import List
from fastapi import Depends, APIRouter
from Database.postgres import getDB
from sqlalchemy.orm import Session
from .helper import  models , curd


router = APIRouter(
    prefix="/countries"
)

@router.get('/getAllCountries')
def getAllCountries(db:Session = Depends(getDB)):
    try:
        return curd.getAllCountries(db=db)
    except :
        print(sys.exc_info())
        return "Something is wrong"

@router.get('/getStates')
def getAllStates( country_code : str | None = None , name : str | None = None , db:Session = Depends(getDB)):
    try:
        if country_code :
            country_code = country_code.upper() 
            return curd.getAllStates(db=db,country_code=country_code) 
        if name :
            name = name.capitalize()
            return curd.getStateByName( db= db , state_name= name )
        return None
    except :
        print(sys.exc_info())
        return "Something is wrong"  

@router.get('/getCities')
def getAllStates( state_id : int | None = None , name : str | None = None , db:Session = Depends(getDB)):
    try:
        if state_id :
            return curd.getCities(db=db,state_id=state_id) 
        if name :
            name = name.capitalize()
            return curd.getCityByName( db = db , city_name=name )
        return True
    except :
        print(sys.exc_info())
        return "Something is wrong"   

@router.get('/addAllCountries')
def addAllCounties(db : Session = Depends(getDB)):
    try:
        file = open('Dataset/Countries.json', encoding="utf8")
        data = json.load(file)
        countries : List[models.Countries] = []
        for d in data :
            countries.append({
                'country_code' : d['iso2'],
                'country_name' : d['name'],
                'country_currency' : d['currency'],
                'is_active' : True,
                'created_by' : 'Himanshu',
                'updated_by' : 'Himanshu',
                'created_date' : datetime.now(),
                'updated_date' : datetime.now()
            })
        curd.add_countries(db=db,countries=countries)
        return True
    except :
        print(sys.exc_info())
        return "Something is wrong"

@router.get('/addAllStates')
def addAllstates(db:Session = Depends(getDB)):
    try:
        file = open('Dataset/States.json', encoding="utf8")
        data = json.load(file)
        states : List[models.States] = []
        for d in data :
            states.append({
                'state_id' : d['id'],
                'country_code' : d['country_code'],
                'state_name' : d['name'],
                'state_code' : d['state_code'],
                'is_active' : True,
                'created_by' : 'Himanshu',
                'updated_by' : 'Himanshu',
                'created_date' : datetime.now(),
                'updated_date' : datetime.now()
            })
        curd.add_states(db=db,states=states)
        return True
    except:
        print(sys.exc_info())
        return "Something is wrong"

@router.get('/addAllCities')
def addAllstates(db:Session = Depends(getDB)):
    try:
        file = open('Dataset/Cities.json', encoding="utf8")
        data = json.load(file)
        cities : List[models.City] = []
        for d in data :
            cities.append({
                'city_id' : int(d['id']),
                'state_id' : d['state_id'],
                'city_name' : d['name'],
                'city_code' : d['wikiDataId'],
                'is_active' : True,
                'created_by' : 'Himanshu',
                'updated_by' : 'Himanshu',
                'created_date' : datetime.now(),
                'updated_date' : datetime.now()
            })
        curd.add_cities(db=db,cities=cities)
        return True
    except:
        print(sys.exc_info())
        return "Something is wrong"