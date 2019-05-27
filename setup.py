import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'sqlalchemy',
    'waitress',
    'zope.sqlalchemy',
    'bcrypt',
    'alembic',
    'sqlalchemy_utils',
    'passlib',
    'webtest',
    'pycodestyle',
    'pytest'
]

setup(name='easy_webserver',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = easy_webserver:main
      """,
)