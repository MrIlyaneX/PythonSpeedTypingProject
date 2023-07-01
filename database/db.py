import sqlalchemy as db
from sqlalchemy import DATETIME, Boolean
from datetime import datetime
from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
# url = "sqlite:///database/mydb.db"
url = "sqlite:///mydb.db"


class UserDB(Base):
    """
        Class User contains his unique ID (we do not need to set it), username, password and
        ID of his achievements. We need username, password, email, and disabled mark for
        creating an object. Describes the main information about users.
    """
    __tablename__ = "Users"

    id = Column("id", Integer, primary_key=True)
    username = Column("username", String)
    password = Column("password", String)
    email = Column("email", String)
    disabled = Column("disabled", Boolean)

    def __init__(self, name: str, password: str, email: str):
        self.username = name
        self.password = password
        self.email = email
        self.disabled = False
        self.attempts = [0]
        ach = Achievements()
        session.add(ach)
        session.commit()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, " \
               f"password={self.password}, email={self.email!r}, disabled={self.disabled!r})"


class Achievements(Base):
    """
        Class Achievements contains unique id, max speed without mistakes(double), days in a raw(integer),
        max symbols in one day (integer), time spend on site (integer), last visit (DATETIME).
        Firstly, all the attributes are set to 0, 1, or today date. Represents all current achievements
        of the corresponding user (their ids are the same)
    """
    __tablename__ = 'Achievements'
    id = Column("id", Integer, primary_key=True)
    max_score = Column("max_score", Integer)
    avg_accuracy = Column("avg_accuracy", Double)
    days_in_raw = Column("days_in_raw", Integer)
    max_days_in_raw = Column("max_days_in_raw", Integer)
    max_symbols_per_day = Column("max_symbols_per_day", Integer)
    time_spend = Column("time_spend", Integer)
    last_visit = Column("last_visit", DATETIME)
    level = Column("level", Integer)

    def __init__(self):
        self.max_score = 0
        self.avg_accuracy = 0
        self.days_in_raw = 1
        self.max_days_in_raw = 1
        self.max_symbols_per_day = 0
        self.time_spend = 0
        self.last_visit = datetime.utcnow()
        self.level = 1

    def __repr__(self) -> str:
        return f"Achievements(average accuracy = {self.avg_accuracy}, max score = {self.max_score}, " \
               f"days in raw = {self.days_in_raw}, max days in raw = {self.max_days_in_raw}, " \
               f"max symbols per day = {self.max_symbols_per_day}, spent time={self.time_spend}, " \
               f"last visit={self.last_visit}, level = {self.level}"


engine = db.create_engine(url, echo=False)
meta = Base.metadata
meta.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


""" Variable for saving 10 users with the best max_scores in tuple type (username, score). """
top = [("", 0)]


# person1 = UserDB('Ann', '1234', 'em1')
# person2 = UserDB('Kate', '3456', 'em2')
# person3 = UserDB('Dan', '7890', 'em3')
# session.add(person1)
# session.add(person2)
# session.add(person3)
# session.commit()


def get_person_by_username(username: str) -> dict | None:
    """ Finds the needed user by his username and returns a dictionary with his personal
    information and achievements if such username exists. Otherwise, returns None. """
    current_user: UserDB = session.query(UserDB).filter_by(username=username).scalar()
    if current_user is None:
        return None
    current_achievements = session.get(Achievements, current_user.id)
    return {
        "username": current_user.username,
        "email": current_user.email,
        "disabled": current_user.disabled,
        "hashed_password": current_user.password,
        "achievements": {
            "max_score": current_achievements.max_score,
            "avg_accuracy": current_achievements.avg_accuracy,
            "max_speed_accuracy": 0,
            "last_visit": current_achievements.last_visit,
            "max_symbols_per_day": current_achievements.max_symbols_per_day
        }
    }


def get(username: str) -> UserDB | None:
    """ Finds the user in the table and returns UserDB object if he exists.
        Used for inside processes. """
    current_user: UserDB = session.query(UserDB).filter_by(username=username).scalar()
    if current_user is None:
        return None
    return current_user


def get_achievements(username: str) -> Achievements | None:
    """ Finds the corresponding user and his achievements using his id.
    Returns Achievements object, used for inside processes. """
    current_user = get(username)
    return session.get(Achievements, current_user.id)


def get_top() -> list:
    """ Returns the top of 10 users with the best scores. """
    return top


def add_person(username: str, password: str, mail: str) -> None:
    """ Creates a new UserDB object and puts him into the table. """
    new_person = UserDB(username, password, mail)
    session.add(new_person)
    session.commit()


def set_username(old: str, new: str) -> None:
    """ Changes the username of the user """
    person = get(old)
    if person is not None:
        person.username = new
        session.commit()
    else:
        return None


def set_password(old: str, new: str) -> None:
    """ Changes the password of the user """
    person = get(old)
    if person is not None:
        person.password = new
        session.commit()
    else:
        return None


def set_achieve(data: dict, username: str) -> None:
    user = get(username)
    achieve = get_achievements(username)
    achieve.avg_accuracy = max(achieve.avg_accuracy, data['avg_accuracy'])
    achieve.max_score = max(achieve.max_score, data['max_score'])
    achieve.max_symbols_per_day = max(achieve.max_symbols_per_day, data['max_symbols_per_day'])
    achieve.time_spend = data['time_spend']
    achieve.last_visit = data['last_visit']
    session.commit()
    if data['max_score'] > top[0][1]:
        top.append((username, data['max_score']))
        sorted(top, key=lambda current_user: current_user[1])
        if top.__len__() > 10:
            top.pop()
    user.attemts.append(data['max_score'])
    user.attempts.pop()
    session.commit()
