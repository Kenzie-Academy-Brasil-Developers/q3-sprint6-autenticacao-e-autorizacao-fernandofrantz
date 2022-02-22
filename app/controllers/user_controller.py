from flask import current_app, request
from app.models.user_model import UserModel
from flask_jwt_extended import create_access_token


def create_user():
    pass
    new_user_data = request.get_json()

    user_to_create = UserModel(**new_user_data)

    access_token = create_access_token(identity=user_to_create.serializer())
    print(user_to_create.serializer())
    print(access_token)
    return ''

    # print(access_token)
    # current_app.db.session.add(user_to_create)
    # current_app.db.session.commit()





def get_user():
    pass
