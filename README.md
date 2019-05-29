# Python-easy-webstack

Starting from scratch for each project is hassle. This is what i personally use as a starting point when creating new web projects.

## Disclaimer

You are yourself responsible for performing the steps neccecary to secure the code from unwanted attackers or data leakage, be it removal of the debug toolbar, or replacing the current signed cookie system. 

By using this package, you agree to perform an audit on the code yourself, and to fix any possible issues before using it live

## Starting the server

The server is made to run under docker. Simply run `docker-compose up` from the root directory. If you want to run specific commands against the container, use `docker-compose run web <command>`. This is useful for running tests etc. If you for some reason want to avoid docker, or if you want to port it to another containerization system, simply use `docker-compose.yml` and `Dockerfile` as documentation as to how the server is set up.

## Overview of the folders

```
.
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 7093dd9953e6_added_the_concept_of_a_user.py
├── alembic-docker.ini
├── alembic.ini
├── CHANGES.txt
├── docker-compose.yml
├── Dockerfile
├── docker-pyramid.ini
├── docker-startup.sh
├── easy_webserver
│   ├── auth.py
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── security.py
│   ├── static
│   │   └── main.css
│   ├── templates
│   │   ├── index.jinja2
│   │   ├── layout.jinja2
│   │   ├── login.jinja2
│   │   └── registrer.jinja2
│   ├── tests.py
│   └── views.py
├── LICENSE
├── MANIFEST.in
├── pyramid-docker.ini
├── pytest.ini
├── README.md
└── setup.py

```

 * `alembic` contains database migrations. This is how you modify your database, even in production, with live data, automatically. Magic!
 * `easy_webserver` contains the web server
   - `models` contains the python representation of the database tables, for use with ORM
   - `static` contains static files that are to be statically served
   - `templates` contains jinja templates that are evaluated to display content for users
   - `__init__.py` sets up the web server, including what views to show
   - `views.py` contains code for generating the correct data context for the different views


## Steps to develop your own stuff

New pyramid views goes in `views.py`, and are registered in `__init__.py`. Pyramid allows you to do all kinds of cool stuff, so be sure to check the documentation.

In order to create alembic migrations(needed for the actual database to be updated when you change a model), run `docker-compose run web alembic revision --autogenerate -m "Revision name"`. This will auto-detect changes. Be sure to look over what changes were detected before actually applying it.


## Relevant documentation

### Pyramid

 * Most of the stuff i have written is based on this [Quick tutorial for Pyramid](https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html)

### Using alembic

 * See http://alembic.zzzcomputing.com/en/latest/tutorial.html
 * See http://alembic.zzzcomputing.com/en/latest/autogenerate.html for autogeneration

### Jinja

 * http://jinja.pocoo.org/docs/2.10/templates/