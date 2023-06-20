import sqlalchemy as db
from sqlalchemy import select, DATETIME, Boolean
from datetime import datetime
from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.orm import declarative_base, sessionmaker

""" I don't know how to create a table inside another table. So I just create an object "Achieves" 
    inside the __init__ function and remember it's id in the variable for getting information from it.
    You can use ID of user for getting his achievements:

    gotten_person = session.get(User, 2)   -- here we get the user using his ID
    ach = session.get(Achieves, gotten_person.ach_id)    -- here we get his achievements
"""

Base = declarative_base()

"""
    Class User contains his unique ID (we do not need to set it), username, password and 
    ID of his achievements. We need username and password for creating an object.
"""


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    username = Column("username", String)
    password = Column("password", String)
    email = Column("email", String)
    disables = Column("disabled", Boolean)

    def __init__(self, name, password, email):
        self.username = name
        self.password = password
        self.email = email
        self.disables = False
        ach = Achieves()
        session.add(ach)
        session.commit()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.name!r}, " \
               f"password={self.password})"


""" 
    Class Achieves contains unique id, max speed without mistakes(double), days in a raw(integer), 
    max symbols in one day (integer), time spend on site (integer), last visit (Integer) (Should we make
    it as a Date?). Firstly, all the attributes ate set to 0.
    
    Also, because of my method of relating the User object and Achieves object I cannot set the column
    owner_id in Achieves. Is that a problem? Do we need the owner id of achievements? (actually, 
    in my opinion, we don't)
    
    Anyway, I can set the owner id after "commit" function, if it needed.
"""


class Achieves(Base):
    __tablename__ = 'Achievements'
    id = Column(Integer, primary_key=True)
    max_score = Column(Integer)
    avg_accuracy = Column(Double)
    days_in_raw = Column(Integer)
    max_days_in_raw = Column(Integer)
    max_symbol_per_day = Column(Integer)
    time_spend = Column(Integer)
    last_visit = Column(DATETIME)
    level = Column(Integer)

    def __init__(self):
        self.max_score = 0
        self.avg_accuracy = 0
        self.days_in_raw = 1
        self.max_days_in_raw = 1
        self.max_symbol_per_day = 0
        self.time_spend = 0
        self.last_visit = datetime.utcnow()
        self.level = 1

    def __repr__(self):
        return f"Achievements(speed = {self.avg_accuracy}, days = {self.days_in_raw}," \
               f" max symbols = {self.max_symbol_per_day}, time = {self.time_spend}, " \
               f"last visit = {self.last_visit}"


engine = db.create_engine("sqlite:///mydb.db", echo=True)
connection = engine.connect()
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind = engine)
session = Session()

person1 = User('Ann', '1234', 'em1')
person2 = User('Kate', '3456', 'em2')
person3 = User('Dan', '7890', 'em3')
session.add(person1)
session.add(person2)
session.add(person3)
session.commit()


def get_person_by_id(id):
    return session.get(User, id)


def get_person_by_username(username) -> User:
    return session.execute(select(User).filter_by(username=username)).scalar_one()


def get_achieves(name):
    person = get_person_by_username(name)
    return session.get(Achieves, person.id)


def add_person(username, password):
    new_person = User(username, password)
    session.add(new_person)
    session.commit()


def set_username(old, new):
    person = get_person_by_username(old)
    person.username = new
    session.commit()


def set_password(old, new):
    person = get_person_by_username(old)
    person.password = new
    session.commit()


def set_achieve(kind, name, value):
    achieve = get_achieves(name)
    if kind == 'avg_accuracy':
        achieve.avg_accuracy = max(achieve.avg_accuracy, value)
    elif kind == 'max_score':
        achieve.max_score = max(achieve.max_score, value)
    elif kind == 'days_in_raw':
        achieve.days_in_raw = value
    elif kind == 'max_symbol_per_day':
        achieve.max_symbol_per_day = value
    elif kind == 'time_spend':
        achieve.time_spend += value
    elif kind == 'last_visit':
        achieve.last_visit = value
    elif kind == 'level':
        achieve.level += 1
    session.commit()
