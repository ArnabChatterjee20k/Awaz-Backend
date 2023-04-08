from ..db.db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..utils.Token import get_password_hash
from .Contacts import Contacts
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, nullable=False)
    voice = Column(String)
    __password = Column(String,nullable=False)
    
    contacts = relationship("Contacts", backref="user")

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,value):
        self.__password = get_password_hash(value)