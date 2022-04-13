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
    new_data = {}
    
    keys_expected = {'cpf', 'name', 'vaccine_name', 'health_unit_name'}
    for key, value in data.items():
        if key in keys_expected:
            new_data[key] = value
            
    
    new_data['first_shot_date'] = datetime.datetime.now()
    new_data['second_shot_date'] = new_data['first_shot_date'] + datetime.timedelta(days=90)
    
    try: 
        vaccine = VaccineCard(**new_data)
                
        session: Session = db.session()
        session.add(vaccine)
        session.commit()
    except IntegrityError as e:
        if  f'{type(e.orig)}' == "<class 'psycopg2.errors.CheckViolation'>":
            return {'error': 'the values passed must be string and must contain 11 characters'}, HTTPStatus.BAD_REQUEST
        elif f'{type(e.orig)}' == "<class 'psycopg2.errors.UniqueViolation'>":
            return {'error': 'cpf already existent'}, HTTPStatus.CONFLICT
        elif f'{type(e.orig)}' == "<class 'psycopg2.errors.NotNullViolation'>":
            receveid_keys = [key for key in data.keys()]
            return {'error': f"expected to receive ['cpf', 'name', 'vaccine_name', 'health_unit_name'], instead received {receveid_keys}"}, HTTPStatus.BAD_REQUEST
 
          
    return jsonify(vaccine), HTTPStatus.CREATED

def retrieve_vaccination():
    session: Session = db.session()
    vaccines = session.query(VaccineCard).all()
    
    return jsonify(vaccines), HTTPStatus.OK