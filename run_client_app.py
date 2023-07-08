from Client.user.qt_runner import setup_windows

# pyinstaller --onefile --noconsole --add-data "Client;Client" ./run_client_app.py

if __name__ == '__main__':
    """ Run the client application. """
    setup_windows()
