#!/bin/env/python
# -*- coding: utf-8 -*-
# http://docs.pylonsproject.org/projects/pyramid/dev/narr/testing.html
#                                            #creating-functional-tests
import unittest
import transaction


class AccountantsFunctionalTests(unittest.TestCase):
    """
    these tests are functional tests to check functionality of the whole app
    (i.e. integration tests)
    they also serve to get coverage for 'main'
    """
    def setUp(self):
        my_settings = {'sqlalchemy.url': 'sqlite://',
                       'available_languages': 'da de en es fr'}
        #my_other_settings = {'sqlalchemy.url': 'sqlite:///test.db',
        #                     'available_languages': 'da de en es fr'}
                        # mock, not even used!?
        #from sqlalchemy import engine_from_config
        #engine = engine_from_config(my_settings)

        from pyramidonal import main
        #try:
        app = main({}, **my_settings)
        #except:
        #    app = main({}, **my_other_settings)
        #    pass
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        # maybe I need to check and remove globals here,
        # so the other tests are not compromised
        #del engine
        #from pyramidonal.model import DBSession
        #DBSession.remove()
        #DBSession.close()
        pass

    def test_root(self):
        """
        load the front page
        """
        res = self.testapp.get('/', status=200)
        #print res.body
        self.failUnless('Home' in res.body)
        # submit a form
        #form = res.form
        #form['login'] = 'foo'
        #form['password'] = 'bar'
        #res2 = form.submit('submit')
        #self.failUnless(
        #    'Please note: There were errors' in res2.body)
        # try valid user & invalid password
        #form = res2.form
        #form['login'] = 'rut'
        #form['password'] = 'berry'
        #res3 = form.submit('submit', status=200)

    def test_persons(self):
        """
        load the page about persons
        """
        res = self.testapp.get('/persons.html', status=200)
        print res.body
        self.failUnless('Persons' in res.body)

    def test_persons_plusone(self):
        """
        add a person
        """
        res = self.testapp.get('/create_person', status=200)
        self.failUnless("Added" in res.body)
        #print(res.body)
        names = res.body.split(' ')
        firstnames = [
            'Donald', 'Gustav', 'Dagobert', 'Walter', 'Brian', 'Holger']
        self.failUnless(
            names[1] in firstnames)
        #self.failUnless('Holger' in res.body)  # not always true
