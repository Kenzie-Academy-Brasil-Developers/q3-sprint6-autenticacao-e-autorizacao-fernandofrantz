from sqlalchemy import VARCHAR, Column, String, Integer, column, false, null
from app.configs.database import db

class UserModel(db.Model):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    last_name: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
    password_hash: str = Column(String, nullable=False)
    api_key: str = Column(String, nullable=False)

    def serializer(self):
        return {
            "name": self.name
        }
