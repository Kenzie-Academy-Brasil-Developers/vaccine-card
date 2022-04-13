from app.configs.database import db
from sqlalchemy import Column, String, DateTime, CheckConstraint
from dataclasses import dataclass


@dataclass
class VaccineCard(db.Model):
    cpf: str
    name: str
    first_shot_date: str
    second_shot_date:str
    health_unit_name: str
    
    __tablename__ = 'vaccine_cards'
    
    cpf = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String, nullable=False)
    
    
    
    