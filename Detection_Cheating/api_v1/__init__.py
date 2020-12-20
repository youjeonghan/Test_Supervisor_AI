from flask import Blueprint

api = Blueprint("api", __name__)

from api_v1 import auth
from api_v1 import student
from api_v1 import analysis