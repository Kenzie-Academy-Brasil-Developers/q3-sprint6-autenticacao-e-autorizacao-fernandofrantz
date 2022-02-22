from flask import Blueprint

from app.controllers.user_controller import create_user, get_user

bp_user = Blueprint('bp_user', __name__, url_prefix='/api')

bp_user.post('/users')(create_user)
bp_user.get('/users')(get_user)
