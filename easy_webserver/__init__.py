from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from easy_webserver.models import db, Base
from pyramid.session import SignedCookieSessionFactory

import logging
log = logging.getLogger(__name__)


def main(global_config, **settings):
    log.debug("Hello! The server is starting")
    engine = engine_from_config(settings, 'sqlalchemy.')
    db.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    config.include('pyramid_jinja2')
    config.include('.security')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('images', '/uploads', cache_max_age=3600)

    # Pages
    config.add_route('home', '/')

    config.add_route('new_auction', '/auction/new')
    config.add_route('login', '/login')
    config.add_route('profile', '/profile')
    config.add_route('admin', '/admin')
    config.add_route('auction', '/auction/{auctionid}')

    config.add_route('registrer', '/register')

    # Rest api
    config.add_route("rest_user_login", "/rest/user/login")
    config.add_route("rest_user_logout", "/rest/user/logout")

    config.add_route("user_create", "/rest/user/create")
    config.add_route("user_delete", "/rest/user/{id}/delete")

    config.scan()

    # Set up cookies
    my_session_factory = SignedCookieSessionFactory('test')
    config.set_session_factory(my_session_factory)

    print("Successfully configured pyramid")

    # config.scan('.views')
    return config.make_wsgi_app()
