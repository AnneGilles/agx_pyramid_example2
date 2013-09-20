#!/bin/bash

virtualenv env
env/bin/pip install --upgrade setuptools
env/bin/python bootstrap.py
bin/buildout
bin/test
