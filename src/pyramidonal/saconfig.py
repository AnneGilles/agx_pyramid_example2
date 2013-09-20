# -*- coding: utf-8 -*-
from z3c.saconfig.interfaces import (
    IEngineCreatedEvent,
    IEngineFactory,
)
from zope import component
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@component.adapter(IEngineCreatedEvent)
def engineCreatedHandler(event):
    fact = component.queryUtility(IEngineFactory, 'default')
    if fact and fact._args == event.engine_args:
        Base.metadata.create_all(event.engine)

component.provideHandler(engineCreatedHandler)