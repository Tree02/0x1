import sqlite3

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = sqlalchemy.create_engine("sqlite:///database.db")
base = declarative_base()

class database():
    """historial de gastos"""
    __tablename__ = "historial"
    id  = Column(Integer, primary_key = True)
    description = Column(String)
    mount = Column(Float)
    def __repr__(self):
        pass

def addi(x):
    database.add(x)

if __name__ == "__main__":
    base.metadata.create_all(engine)
    