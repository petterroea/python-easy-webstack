# Python-easy-webstack

Starting from scratch for each project is hassle. This is what i personally use as a starting point when creating new web projects.

## Starting the server

The server is made to run under docker. Simply run `docker-compose up` from the root directory. If you want to run specific commands against the container, use `docker-compose run web <command>`. This is useful for running tests etc. If you for some reason want to avoid docker, or if you want to port it to another containerization system, simply use `docker-compose.yml` and `Dockerfile` as documentation as to how the server is set up.

## Overview of the folders

```

```



## Steps to develop your own stuff

New pyramid views goes in `views.py`

## Relevant documentation

### Pyramid

 * Most of the stuff i have written is based on this [Quick tutorial for Pyramid](https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html)

### Using alembic

 * See http://alembic.zzzcomputing.com/en/latest/tutorial.html
 * See http://alembic.zzzcomputing.com/en/latest/autogenerate.html for autogeneration
