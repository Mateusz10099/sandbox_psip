# --- DML --- #

import random

import sqlalchemy
import os
import sqlalchemy.orm
from dotenv import load_dotenv
from geoalchemy2 import Geometry
from faker import Faker

load_dotenv()

#tworzę plik o nazwie .env
db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_BD"),
    port=os.getenv("POSTGRES_PORT"),
)

engine = sqlalchemy.create_engine(db_params)
conection = engine.connect()

Base = sqlalchemy.orm.declarative_base()

# uwaga trzeba pamiętać o dodaniu extension
class User(Base):
    __tablename__ = 'aaa'

    id = sqlalchemy.Column(sqlalchemy.Integer(),primary_key=True) # serial
    name = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    location = sqlalchemy.Column('geom' , Geometry(geometry_type="POINT", srid=4326), nullable=True)

Base.metadata.create_all(engine)

conection.close()
engine.dispose()