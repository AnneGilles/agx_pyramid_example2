# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship
from pyramidonal.saconfig import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Sequence,
)

class Person(Base):

    __tablename__ = 'person'
    id = Column(Integer,index = True, primary_key = True)
    firstname = Column(String)
    lastname = Column(String)
    addresses = relationship('Address', cascade = 'all, delete-orphan', backref = 'person', primaryjoin = 'Address.person_id == Person.id')

class Address(Base):

    __tablename__ = 'address'
    id = Column(Integer,index = True, primary_key = True)
    city = Column(String)
    zip = Column(String)
    street = Column(String)
    country = Column(String)
    person_id = Column(Integer, ForeignKey('person.id'), nullable = False)