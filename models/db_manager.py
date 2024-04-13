from sqlalchemy import create_engine, MetaData, Column, INTEGER, TEXT, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from config import DB_URL

db = create_engine(DB_URL, echo=False)
Session = sessionmaker(bind=db)
session = Session()
metadata = MetaData(bind=db)
Base = declarative_base(metadata=metadata)
Model=Base
