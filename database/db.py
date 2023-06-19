import sqlalchemy as db
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    username = Column("username", String)
    password = Column("password", String)
    achievements = Column(String)

    def __init__(self, name, password, a):
        self.username = name
        self.password = password
        self.achievements = a

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.name!r}, " \
               f"password={self.password})"


class Achieves(Base):
    __tablename__ = 'Achievements'
    id = Column(Integer, primary_key=True)
    speed_no_mistakes = Column(Integer)
    days_in_raw = Column(Integer)
    max_symbol_one_day = Column(Integer)
    time_on_site = Column(Integer)
    last_visit = Column(Integer)
    owner = Column(Integer, ForeignKey("Users.id"))

    def __init__(self, owner_id):
        self.speed_no_mistakes = 0
        self.days_in_raw = 0
        self.max_symbol_one_day = 0
        self.time_on_site = 0
        self.last_visit = 0
        self.owner = owner_id


    def __repr__(self):
        return f"Achievements(spees = {self.speed_no_mistakes}, days = {self.days_in_raw}," \
               f" max symbols = {self.max_symbol_one_day}, time = {self.time_on_site}, " \
               f"last visit = {self.last_visit}"


engine = db.create_engine("sqlite:///mydb.db", echo=True)
connection = engine.connect()
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind = engine)
session = Session()


# person1 = User('Ann', '1234', 'no')
# person2 = User('Kate', '3456', 'no')
# person3 = User('Dan', '7890', 'no')
# session.add(person1)
# session.add(person2)
# session.add(person3)
# session.commit()

a1 = Achieves(1)
a2 = Achieves(2)
a3 = Achieves(3)
session.add(a1)
session.add(a2)
session.add(a3)
session.commit()

gotten_person = session.get(User, 1)
print(gotten_person.username, gotten_person.password)


def get_person(id):
    return session.get(id)


def set_person(username, password):
    new_person = User(username, password)
    session.add(new_person)
    session.commit()


# Creation of an object
# user1 = User(username = 'Ivan')
# session.add(user1)
# session.commit()
# print(user1.id)
#
# # Getting info from the base
# q = session.query(User).filter_by(username = 'Ivan')
# gotten_user = q.first()
# # gotten_user is user1 = True
#
# #Mutation:
# user1.username = 'Vasya'
# session.commit()




# user: unique id, username, password, achievements - table
# achievements:
# max speed without mistakes
# days in a row
# max symbols in one day
# time spent on site
# last visit time