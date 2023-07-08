from pathlib import Path

users_path = Path(Path.cwd()).parent


# def update_user(user: User, logout: bool = False) -> None:
#     user_path = Path(users_path.joinpath(Path("Client/user/data/info.json")))
#     with open(user_path, "w") as info:
#         user.disabled = logout
#         json.dump(user_to_dict(user), info, indent=4)


# def get_user() -> User:
#     user_path = Path(users_path.joinpath(Path("Client/user/data/info.json")))
#     with open(user_path, "r") as info:
#         user = User(**json.load(info))
#         user.disabled = False
#         return user


# def get_password() -> str:
#     pass_path = Path(users_path.joinpath(Path("Client/user/data/password.json")))
#     with open(pass_path, "r") as info:
#         return json.load(info)
