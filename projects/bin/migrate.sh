#!/bin/bash

cd /vagrant/projects
python manage.py makemigrations resume
python manage.py migrate
