import sqlalchemy as db
from sqlalchemy import ForeignKey
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
    achievement_id = Column("achieve id", Integer)

    def __init__(self, name, password):
        self.username = name
        self.password = password
        ach = Achieves()
        session.add(ach)
        session.commit()
        self.achievement_id = ach.id

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
    speed_no_mistakes = Column(Double)
    days_in_raw = Column(Integer)
    max_symbol_one_day = Column(Integer)
    time_on_site = Column(Integer)
    last_visit = Column(Integer)

    owner_id = Column(Integer, ForeignKey("Users.id"))

    def __init__(self):
        self.speed_no_mistakes = 0
        self.days_in_raw = 0
        self.max_symbol_one_day = 0
        self.time_on_site = 0
        self.last_visit = 0

    def __repr__(self):
        return f"Achievements(speed = {self.speed_no_mistakes}, days = {self.days_in_raw}," \
               f" max symbols = {self.max_symbol_one_day}, time = {self.time_on_site}, " \
               f"last visit = {self.last_visit}"


engine = db.create_engine("sqlite:///mydb2.db", echo=True)
connection = engine.connect()
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind = engine)
session = Session()


person1 = User('Ann', '1234')
person2 = User('Kate', '3456')
person3 = User('Dan', '7890')
session.add(person1)
session.add(person2)
session.add(person3)
session.commit()

# Example of getting objects from the database
gotten_person = session.get(User, 2)
ach = session.get(Achieves, gotten_person.achievement_id)
print(gotten_person.username, gotten_person.password, ach.last_visit)


def get_person(id):
    return session.get(id)


def add_person(username, password):
    new_person = User(username, password)
    session.add(new_person)
    session.commit()



# user: unique id, username, password, achievements - table
# achievements:
# max speed without mistakes
# days in a row
# max symbols in one day
# time spent on site
# last visit time