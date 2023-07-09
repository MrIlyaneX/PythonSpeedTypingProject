import requests


class app_updater:
    def __init__(self, url: str = "http://127.0.0.1:8000"):
        self.url = url
        username = "sean_testo_secret_naming_convention"
        password = "some_password_with_no_meaning"
        self.payload = {
            "username": username,
            "password": password
        }

    def update(self, file_path: str = "dist/run_client_app.exe"):
        with open(file_path, "rb") as file:
            response = requests.post(f"{self.url}/token", data=self.payload)
            if response.status_code == 200:
                print("Token received")
                header = {"Authorization": f"Bearer {response.json()['access_token']}"}
            else:
                print(f"Error: {response.status_code}")
                print(response.text)

            response = requests.post(f"{self.url}/make/upload/{self.payload['username']}",
                                     files={"app": file}, headers=header)

        if response.status_code == 200:
            print("File uploaded successfully")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


if __name__ == "__main__":
    updater = app_updater()
    updater.update()
