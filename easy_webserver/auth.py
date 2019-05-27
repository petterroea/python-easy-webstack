from pyramid.httpexceptions import HTTPOk, HTTPFound
from pyramid.security import (
    remember,
    forget,
)
from pyramid.view import (
    forbidden_view_config,
    view_config,
)

from easy_webserver.models.user import User
from easy_webserver.models import db, Base

import json


@view_config(route_name='rest_user_login', renderer='json')
def login(request):
    if not ("login" in request.POST and "password" in request.POST):
        return {"result": False, "message": "Missing parameters"}
    login = request.POST['login']
    password = request.POST['password']

    user = db.query(User).filter(User.email == login).first()

    if user is not None and user.check_password(password):
        headers = remember(request, user.id)
        return HTTPOk(body=json.dumps({"result": True}), headers=headers)

    return {"result": False,
            "message": "The user does not exist, or the password is wrong"}


@view_config(route_name='rest_user_logout', renderer='json')
def logout(request):
    headers = forget(request)
    return HTTPOk(body=json.dumps({"result": True}), headers=headers)


@forbidden_view_config()
def forbidden_view(request):
    next_url = request.route_url('index', _query={'next': request.url})
    return HTTPFound(location=next_url)
