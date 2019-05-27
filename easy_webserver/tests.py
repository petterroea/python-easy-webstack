import unittest

from pyramid import testing

def _initTestingDB():
    from sqlalchemy import create_engine
    from easy_webserver.models import (
        db,
        Base
        )
    from easy_webserver.models.user import User;
    engine = create_engine('postgresql://easy_webserver:example@db/easy_webserver')
    db.configure(bind=engine)
    Base.metadata.bind = engine
    #with transaction.manager:
        #model = Page(title='FrontPage', body='This is the front page')
        #DBSession.add(model)
    return db

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.session = _initTestingDB()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['user'], None)


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import get_app
        app = get_app('pyramid-docker.ini')
        from webtest import TestApp
        self.testapp = TestApp(app)

# Test that all the websites exist
    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'WeText' in res.body)

    def test_upload(self):
        res = self.testapp.get('/upload', status=200)
        self.assertTrue(b'WeText' in res.body)

    def test_reader(self):
        res = self.testapp.get('/reader', status=200)
        self.assertTrue(b'WeText' in res.body)

    def test_profile(self):
        res = self.testapp.get('/profile', status=200)
        self.assertTrue(b'WeText' in res.body)
