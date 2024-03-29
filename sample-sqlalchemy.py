##If you use Zope, you can get the session this way:

#from z3c.saconfig import named_scoped_session
#Session = named_scoped_session('default')
#session=Session()
#session.add(Person(name='Donald Duck')) #assume we have a Person class

##If you use the package standalone, do it that way:

from zope.configuration.xmlconfig import XMLConfig
import zope.component.event  #neccesary to initialize subscription system
import transaction
import pyramidonal
XMLConfig('configure.zcml',pyramidonal)()

#assume we have a few classes in a module 'personal'
from pyramidonal.personal import Person, Company, Address, Employment

from z3c.saconfig import named_scoped_session
Session = named_scoped_session('default')
session=Session()

#now play around with the database
pers=Person(firstname='Donald', lastname='Duck')
pers1=Person(firstname='Dagobert', lastname='Duck')
pers2=Person(firstname='Daisy', lastname='Duck')
session.add_all([pers,pers1,pers2]) #assume we have a Person class

#create 2 companies
comp=Company(name='ACME')
comp1=Company(name='Bluedynamics')
session.add_all([comp,comp1])

#Address for person
pers.addresses.append(Address(street='Erpelstrasse',city='Entenhausen'))

#some different possiblities to establis a relation
comp.employees=[pers]
comp.employees.append(pers1)
comp.employments.append(Employment(employers=comp,employees=pers2, salary=1000))
pers2.employers.append(comp1)

#finally commit everything, now it lands in the db
transaction.commit()

