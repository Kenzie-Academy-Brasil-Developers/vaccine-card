from http import HTTPStatus
from flask import jsonify, request
import datetime 
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import CheckViolation, UniqueViolation

from app.models.vaccine_card_model import VaccineCard
from app.configs.database import db

def create_vaccination():
    data = request.get_json()
    
    keys_expected = {'cpf', 'name', 'vaccine_name', 'health_unit_name'}
    for key in data.keys():
        if not key in keys_expected:
            return {'error': 'invalid keys'}, HTTPStatus.BAD_REQUEST 
    
    
    data['first_shot_date'] = datetime.datetime.now()
    data['second_shot_date'] = data['first_shot_date'] + datetime.timedelta(days=90)
    
    try: 
        vaccine = VaccineCard(**data )
                
        session: Session = db.session()
        session.add(vaccine)
        session.commit()
    except IntegrityError as e:
        if  f'{type(e.orig)}' == "<class 'psycopg2.errors.CheckViolation'>":
            return {'error': 'the values passed must be string'}, HTTPStatus.BAD_REQUEST
        elif f'{type(e.orig)}' == "<class 'psycopg2.errors.UniqueViolation'>":
            return {'error': 'cpf already existent'}, HTTPStatus.CONFLICT
        elif f'{type(e.orig)}' == "<class 'psycopg2.errors.CheckViolation'>":
            return {'error': 'cpf must contain 11 characters'}, HTTPStatus.BAD_REQUEST
 
    
    
        
          
    return jsonify(vaccine), HTTPStatus.CREATED

def retrieve_vaccination():
    session: Session = db.session()
    vaccines = session.query(VaccineCard).all()
    
    return jsonify(vaccines), HTTPStatus.OK