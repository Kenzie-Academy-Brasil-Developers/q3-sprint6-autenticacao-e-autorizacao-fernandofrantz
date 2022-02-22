from inspect import Attribute
from flask import current_app, jsonify, request
from app.models.user_model import UserModel
from flask_jwt_extended import create_access_token
from http import HTTPStatus
from flask_jwt_extended import get_jwt_identity

def create_user():
    pass
    new_user_data = request.get_json()

    password_to_hash = new_user_data.pop("password")

    new_user = UserModel(**new_user_data)

    new_user.password = password_to_hash

    current_app.db.session.add(new_user)
    current_app.db.session.commit()

    return jsonify(new_user.serializer()), HTTPStatus.CREATED


def login_user():
    login_data = request.get_json()

    found_user = UserModel.query.filter(UserModel.email == login_data['email']).first()

    if not found_user:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND

    if (found_user.verify_password(login_data['password'])):

        access_token = create_access_token(identity=found_user.serializer())

        setattr(found_user, "api_key", access_token)

        current_app.db.session.add(found_user)
        current_app.db.session.commit()

        return {"api_key": access_token}, HTTPStatus.OK

    else:
        return {"message": "wrong password"}, HTTPStatus.BAD_GATEWAY

def get_user():
    current_user = get_jwt_identity()
    return jsonify(current_user), HTTPStatus.OK

def patch_user():
    try:
        data = request.get_json()

        user_to_patch = UserModel.query.filter(UserModel.email == data['email']).first()

        patching_data = {
            "name": data['name'],
            "last_name": data['last_name'],
            "email": data['email'],
            "password": data['password']
        }
        
        for key, value in patching_data.items():
            setattr(user_to_patch, key, value)
        
        current_app.db.session.add(user_to_patch)
        current_app.db.session.commit()

        print(patching_data)

        return '', HTTPStatus.OK

    except AttributeError:
        return {"error": "user not found"}, HTTPStatus.NOT_FOUND

def delete_user():
    current_user = get_jwt_identity()

    find_user = UserModel.query.filter(UserModel.email == current_user['email']).first()

    current_app.db.session.delete(find_user)
    current_app.db.session.commit()

    return '', HTTPStatus.NO_CONTENT