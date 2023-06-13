from client import post_user_info, get_user_info
from DB import *

info = [UserInfo(name="mid", id=0), UserInfo(name="Oleg", id=1), UserInfo(name="Dom", id=2)]

info_test = [UserInfo(name="mid", id=0), UserInfo(name="Oleg", id=1),
             UserInfo(name="Dom", id=2), UserInfo(name="Tester", id=3)]


print("Добваляем на сервер через клиента")
for i, user in enumerate(info):
    print(post_user_info(user, i))


print("Забираем информацию с сервера клиентом")
for i in info_test:
    print(get_user_info(i.id))
