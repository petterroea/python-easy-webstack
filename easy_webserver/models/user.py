"""User object"""
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    UniqueConstraint,
    Text,
    Boolean,
    Table
)

from sqlalchemy.orm import relationship

from easy_webserver.models import db
from easy_webserver.models import Base
from datetime import datetime

import bcrypt


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)

    email = Column(Text, nullable=False)
    firstname = Column(Text, nullable=False)
    lastname = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    postal = Column(Integer, nullable=False)

    bids = relationship("Bid")

    def __init__(self, firstname: str, lastname: str,
                 password: str, email: str, gender: str, postal: int):
        self.firstname = firstname
        self.lastname = lastname
        self.password = bcrypt.hashpw(password.encode('utf-8'),
                                      bcrypt.gensalt()).decode('utf-8')
        self.email = email
        self.gender = gender
        self.postal = postal

    def check_password(self, password):
        expected_hash = self.password.encode('utf8')
        return bcrypt.checkpw(password.encode('utf8'), expected_hash)

    def delete_user(self):
        
        db.delete(self)

