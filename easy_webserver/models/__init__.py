from pyramid.security import Allow, Everyone

from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

db = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
