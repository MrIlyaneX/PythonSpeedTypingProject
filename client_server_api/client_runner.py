from DB import *
from client import post_user_info, get_user_info

info = [
    UserInfo(id=0, name="mid", email="mid@example.com", registration_date=datetime.now(),
             achievements={}, last_visit=datetime.now(), days_in_row=0, max_score=0, avg_accuracy=0.0, level=0),
    UserInfo(id=1, name="Oleg", email="oleg@example.com", registration_date=datetime.now(),
             achievements={}, last_visit=datetime.now(), days_in_row=0, max_score=0, avg_accuracy=0.0, level=0),
    UserInfo(id=2, name="Dom", email="dom@example.com", registration_date=datetime.now(),
             achievements={}, last_visit=datetime.now(), days_in_row=0, max_score=0, avg_accuracy=0.0, level=0)
]

info_test = [
    UserInfo(id=0, name="mid", email="mid@example.com", registration_date=datetime.now(),
             achievements={}, last_visit=datetime.now(), days_in_row=0, max_score=0, avg_accuracy=0.0, level=0),
    UserInfo(id=1, name="Oleg", email="oleg@example.com", registration_date=datetime.now(),
             achievements={}, last_visit=datetime.now(), days_in_row=0, max_score=0, avg_accuracy=0.0, level=0),
    UserInfo(id=2, name="Dom", email="dom@example.com", registration_date=datetime.now(),
             achievements={}, last_visit=datetime.now(), days_in_row=0, max_score=0, avg_accuracy=0.0, level=0),
    UserInfo(id=3, name="Tester", email="tester@example.com", registration_date=datetime.now(),
             achievements={}, last_visit=datetime.now(), days_in_row=0, max_score=0, avg_accuracy=0.0, level=0)
]

print("Putting info to api")
for i, user in enumerate(info):
    print(post_user_info(user, i))

print("Getting info from api")
for i in info_test:
    print(get_user_info(i.id))
