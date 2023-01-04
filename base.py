import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Float, DateTime, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from flask import jsonify

engine = sqlalchemy.create_engine("sqlite:///database.db")

base = declarative_base()

class Historial(base):
    __tablename__ = "historial"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    amount = Column(Float)
    date = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return self
    def jsonify(self):
        return ({
            'id' : self.id,
            'description' : self.description,
            'amount' : self.amount,
            'date' : self.date
        })

def insert(descriptionIn, amountIn):
    Session = sessionmaker(bind=engine)
    session = Session()

    a = Historial(description=descriptionIn, amount=amountIn)
    
    session.add(a)
    session.commit()

#Delete id - History // client select, filter id first delete
def deleteId(id):
    Session = sessionmaker(bind=engine)
    session = Session()

    b = session.query(Historial).filter(Historial.id == id).first()

    session.delete(b)
    session.commit()

if __name__ == "__main__":
    base.metadata.create_all(engine)

