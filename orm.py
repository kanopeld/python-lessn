from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///lessn15.sqlite")
Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
session.add(Person(firstname='TEST!!!!', lastname='Varkalov'))
session.add_all([Person('Alex', 'Petrov'), Person('Ann', 'Ivanova')])
session.commit()

persons = session.query(Person).filter_by(firstname="Alex").all()
if persons is None:
    raise Exception('not found')
print(persons)
