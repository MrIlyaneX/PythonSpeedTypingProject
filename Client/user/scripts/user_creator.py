# def signup_user(username: str, email: str, password: str) -> User:
#     def create_password():
#         path = Path(users_path.joinpath(Path("Client/user/data/password.json")))
#         with open(path, "w") as output_password:
#             json.dump({"password": password}, output_password)

#     user = {
#         "username": username,
#         "email": email,
#         "disabled": True,
#         "achievements": {
#             "max_score": 0,
#             "avg_accuracy": 0,
#             "max_speed_accuracy": 0,
#             "last_visit": datetime.utcnow(),
#             "max_symbols_per_day": 0
#         }
#     }

#     user = signup(user_info=User(**user), password=password)

#     update_user(user=user)
#     create_password()
#     return user
