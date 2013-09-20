from sqlalchemy.orm import sessionmaker
import zope.component.event
from zope import component
from zope.configuration.xmlconfig import XMLConfig
from z3c.saconfig.interfaces import IEngineFactory
from zope.sqlalchemy import ZopeTransactionExtension
import transaction

def db(request):
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        transaction.commit()
    request.add_finished_callback(cleanup)

    return session

def config_db(config, engine_name='default', **settings):
    import pyramidonal
    XMLConfig('configure.zcml',pyramidonal)()
    engine=component.getUtility(IEngineFactory,engine_name)()
    config.registry.dbmaker = sessionmaker(bind=engine, extension=ZopeTransactionExtension())
    config.add_request_method(db, reify=True)
