# -*- coding: utf-8 -*-
from pyramid.renderers import get_renderer
from pyramid.response import Response
from pyramid.view import view_config

class ViewTemplate(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        renderer = get_renderer("templates/global_template.pt")
        self.global_template = renderer.implementation()
        self.macros = self.global_template.macros

    @view_config(name='', renderer='templates/home.pt')
    def home(self):
        return {"page_title": "home"}

    @view_config(name='about.html', renderer='templates/about.pt')
    def about(self):
        return {"page_title": "about"}

    @view_config(name='imprint.html', renderer='templates/imprint.pt')
    def imprint(self):
        return {"page_title": "imprint"}

    @view_config(name='persons.html', renderer='templates/persons.pt')
    def persons(self):
        return {"page_title": "persons"}

    def site_menu(self):
        '''static implementation, insert your menu logic here'''
        new_menu = SITE_MENU = [
            {'href': '', 'title': 'Home'},
            {'href': 'about.html', 'title': 'About'},
            {'href': 'imprint.html', 'title': 'Imprint'},
            ]
        
        url = self.request.url
        for menu in new_menu:
            if menu['title'] == 'Home':
                menu['current'] = url.endswith('/')
            else:
                menu['current'] = url.endswith(menu['href'])
                
        return new_menu

    @view_config(name='create_person')
    def create_person(self):
        '''does some silly random person creation'''
        import random
        import model
        firstnames = ['Donald', 'Gustav', 'Dagobert', 'Walter', 'Brian']
        lastnames = ['Duck', 'Smith', 'Gstierbreitner']
        pers = model.Person(firstname=random.choice(firstnames), lastname=random.choice(lastnames))
        self.request.db.add(pers)
        pers.addresses.append(model.Address(city='Entenhausen', street='Erpelweg 13'))
        return Response('Added %s %s' % (pers.firstname, pers.lastname))