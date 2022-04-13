from flask import  Blueprint
from app.controllers import vaccinations_controller

bp = Blueprint('vaccinations', __name__, url_prefix='/vaccinations')

bp.post("")(vaccinations_controller.create_vaccination)
bp.get("")(vaccinations_controller.retrieve_vaccination)
