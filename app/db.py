import os
import sqlalchemy
from sqlalchemy import Table, Column, String
from databases import Database

if os.path.exists('local.db'):
    os.remove('local.db')

engine = sqlalchemy.create_engine('sqlite:///some.db')
metadata = sqlalchemy.MetaData(engine)


tires = Table(
    'tires',
    metadata,
    Column('manufacturer', String),
    Column('season', String),
    Column('profile', String),
)

database = Database('sqlite:///some.db')
