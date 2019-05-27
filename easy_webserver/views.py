from pyramid.view import view_config
from easy_webserver.models.user import User
from easy_webserver.models import db
from datetime import datetime
from datetime import timedelta

from sqlalchemy import or_, and_

import bcrypt
import re
import os
import uuid
import shutil


# For logging that appears in the debug toolbar
import logging
log = logging.getLogger(__name__)


@view_config(route_name='home', renderer='templates/index.jinja2')
def index_view(request):
    user = request.user

    return {"user": user}


@view_config(route_name='login', renderer='templates/login.jinja2')
def login_view(request):
    return {"user": request.user}

@view_config(route_name='registrer', renderer='templates/registrer.jinja2')
def registrer_view(request):
    return {"user": request.user}


# Rest api stuff

@view_config(route_name="user_create", renderer="json")
def create_user_view(request):
    register_variables = request.POST
    if "firstname" not in register_variables \
            or len(register_variables["firstname"]) == 0:
        return {"result": False,
                "message":
                    "You have not filled required fields: First Name"}
    if "lastname" not in register_variables \
            or len(register_variables["lastname"]) == 0:
        return {"result": False,
                "message":
                    "You have not filled required field: Last Name"}
    if "password" not in register_variables \
            or len(register_variables["password"]) == 0:
        return {"result": False,
                "message":
                    "You have not filled required field: Password"}
    if "email" not in register_variables \
            or len(register_variables["email"]) == 0\
            or is_invalid_email(register_variables["email"]):
        return {"result": False,
                "message":
                    "Not a valid email address"}
    if "postal" not in register_variables \
            or len(register_variables["postal"]) != 4:
        return {"result": False,
                "message":
                    "You have not filled required field: Postal (4 numbers)"}
    if "gender" not in register_variables:
        return {"result": False,
                "message":
                    "You have not filled required field: Gender"}
    if request.user:
        return {"result": False, "message": "Already logged in"}
    if not db.query(User) \
             .filter(User.email == register_variables.get("email")) \
             .first() is None:
        return {"result": False, "message": "User already exists"}

    userObj = User(register_variables["firstname"],
                   register_variables.get("lastname"),
                   register_variables.get("password"),
                   register_variables.get("email"),
                   register_variables["gender"],
                   register_variables["postal"])
    db.add(userObj)
    return {"result": True}


def is_invalid_email(email):
    if len(email) > 7:
        if re.match(r"^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$",
                    email) is not None:
            return False
    return True


@view_config(route_name="user_delete", renderer="json")
def user_delete(request):
    _user_object = db.query(User).filter(
        User.id == request.matchdict["id"]).first()

    if request.user is None:
        return {"result": False, "message": "You are not logged in."}

    elif request.user.rank < 1 and _user_object != request.user:
        return {"result": False, "message":
                "You don't have the access rights."}

    _user_object.delete_user()
    return {"result": True, "message": "User deleted."}

