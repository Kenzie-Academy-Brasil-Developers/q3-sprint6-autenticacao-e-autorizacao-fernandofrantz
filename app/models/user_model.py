from sqlalchemy import Column, String, Integer
from app.configs.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    last_name: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
    password_hash: str = Column(String, nullable=True)

    def serializer(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
        }

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
