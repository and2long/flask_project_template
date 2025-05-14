from flask import Blueprint, request

from src.models import db
from src.models.user import User

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('', methods=['GET'])
def index():
    users = User.query.all()
    return [item.to_dict() for item in users]

