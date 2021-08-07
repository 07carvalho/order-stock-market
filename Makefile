activate:
	poetry shell

install/python:
	poetry install

copy/local/envs:
	cp .env.dev .env

run/django:
	python server/manage.py runserver 0.0.0.0:8000
