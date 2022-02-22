from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.user_controller import create_user, delete_user, get_user, login_user, patch_user

bp_user = Blueprint('bp_user', __name__, url_prefix='/api')

bp_user.post('/signup')(create_user)
bp_user.post('/signin')(login_user)

@bp_user.get('')
@jwt_required()
def get():
    return get_user()

@bp_user.patch('')
@jwt_required()
def patch():
    return patch_user()

@bp_user.delete('')
@jwt_required()
def delete():
    return delete_user()