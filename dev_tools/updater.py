import json

import requests


class AppUpdater:
    """
    This class is used to update the app on the server.

    :param url: The URL of the server.
    """

    def __init__(self, url: str = "http://127.0.0.1:8000"):
        self.url = url
        self.payload = {
            "username": "sean_testo_secret_naming_convention",
            "password": "some_password_with_no_meaning"
        }

    def update(self, changes: str, file_path: str = r"../dist/run_client_app.exe"):
        """
        Uploads the client application and appends changes to the history.json file.

        :param file_path: The path to the client application.
        :param changes: The changes made to the client application, stored in a file.
        :return: A dictionary indicating the success of the upload.
        """

        token_response = requests.post(f"{self.url}/token", data=self.payload)
        if token_response.status_code == 200:
            print("Token received")
            header = {"Authorization": f"Bearer {token_response.json()['access_token']}"}
        else:
            print(f"Error: {token_response.status_code}")
            print(token_response.text)
            return

        with open(file_path, "rb") as file:
            with open(changes, "r") as changes_file:
                changes_data = json.load(changes_file)
                changes_payload = changes_data

                files = {
                    "app": file,
                    "changes": json.dumps(changes_payload)
                }

                response = requests.post(
                    f"{self.url}/make/upload/{self.payload['username']}",
                    files=files,
                    headers=header
                )

        if response.status_code == 200:
            print("File uploaded successfully")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


if __name__ == "__main__":
    def main():
        updater = AppUpdater()
        updater.update(changes="changes.json")


    main()
