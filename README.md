# Python Speed Typing Project

This repository contains a desktop-web application developed by a team of four students from Innopolis University. The
project was created as part of an elective course and aims to provide a platform for practicing speed typing and
learning blind typing techniques.

## Project Overview

The Python Speed Typing Project is a desktop-web application designed to improve users' typing skills through a series
of interactive exercises. The application incorporates the principles of speed typing and offers a user-friendly
interface for practicing and tracking progress.

## Features

- **Speed Typing Exercises**: The application provides a variety of exercises to improve typing speed and accuracy.
  Users can choose from different difficulty levels and practice typing paragraphs, sentences, or random words.

- **Blind Typing Techniques**: The application includes exercises specifically tailored to help users learn and master
  blind typing techniques. These exercises focus on typing without looking at the keyboard, enhancing muscle memory and
  typing efficiency.

- **Performance Tracking**: Users can track their typing speed, accuracy, and progress over time. The application
  records and displays various metrics, allowing users to monitor their improvement and set personal goals.

## Installation

- ### By download from our server (Not working)

To download the Python Speed Typing app, you can visit our server and follow these steps:

1. Go to [our website](https://) in your web browser.

2. Click on the download button to initiate the download of the app.

By downloading the Python Speed Typing app from our server, you can enjoy the features and improve your typing skills.

If you encounter any issues during the download or installation process, please reach out to our support team for
assistance.

We appreciate your interest in the Python Speed Typing Project and hope you find the app helpful in improving your
typing skills.

- ### By using local machine:

To install the Python Speed Typing Project, you can use `pip` to install the required dependencies. Here are the steps:

1. Make sure you have Python installed on your machine. You can download Python from
   the [official website](https://www.python.org/downloads/).

2. Clone the repository to your local machine or download the source code as a ZIP file.

3. Open a terminal or command prompt and navigate to the project's root directory.

4. Create a virtual environment (optional but recommended) to isolate the project's dependencies. You can create a
   virtual environment by running the following command:

```commandline
python -m venv env
```

This will create a new directory called `env` containing the virtual environment.

5. Activate the virtual environment. On Windows, run:

```commandline
env\Scripts\activate
```

On macOS and Linux, run:

```commandline
source env/bin/activate
```

6. Install the project dependencies using `pip`. Run the following command:

  ```commandline
    pip install -r requirements.txt
  ```

This will install all the necessary libraries and frameworks, including FastAPI and PyQt.

7. Once the installation is complete, you can run the Python Speed Typing Project using the appropriate commands for
   your specific setup.

- For running the FastAPI server, use:

  ```
  uvicorn app.main:app --reload
  ```

  This will start the server, and you can access the endpoints through the provided URLs.

- For running the desktop application, follow the instructions specific to your operating system and the PyQt framework.

  Note: Additional setup may be required depending on the desktop application's specific requirements and dependencies.

## Technologies Used

The Python Speed Typing Project utilizes the following libraries and frameworks:

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.

- **PyQt**: A comprehensive set of Python bindings for the Qt application framework, allowing for the creation of
  cross-platform desktop applications.

-

-

## Endpoints

The Python Speed Typing Project provides the following endpoints:

- `POST /token`: Retrieves an access token for the user based on the provided login credentials.

- `GET /users/me/`: Retrieve the details of the current authenticated user.

- `POST /users/me/upload`: Upload data for the current authenticated user.

- `POST /signup/{username}/{user_email}/{password}`: Sign up a new user.

- `GET /files/words/{language}`: Retrieve words for a specific language.

- `POST /leaderboard`: Posts the leaderboard (10 best scores) to the client.

- `GET /download`: Downloads the client application.

- `GET /`: Retrieves the index page.

- `POST /make/upload/{username}`: Uploads the client application and appends changes to the history.json file.

Please refer to the API documentation for more details on each endpoint.

## Contact

If you have any questions or need further assistance, please contact the project team:

- Ilia Mistiurin
- Elena Tesmeeva
- Polina Pushkareva
- Anastasia Pichugina

Thank you for your interest in the Python Speed Typing Project! We hope you find it helpful in improving your typing
skills.
