import os


def run_script():
    root_directory = r'C:\Users\misty\PycharmProjects\PythonTeamFastAPI'
    output_file = 'folder_structure.txt'
    gitignore_file = r'C:\Users\misty\PycharmProjects\PythonTeamFastAPI\.gitignore'

    def print_directory_structure(directory=root_directory, indent='', ignore_list=None):
        if ignore_list is None:
            ignore_list = []

        ignore_list.extend(['__pycache__', '.git', 'venv'])

        with open(output_file, 'a', encoding='utf-8') as file:
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if item != '__pycache__':
                    if os.path.isdir(item_path):
                        if item not in ignore_list:
                            file.write(indent + '├── ' + item + '/' + '\n')
                            print_directory_structure(item_path, indent + '│   ', ignore_list)
                    else:
                        file.write(indent + '├── ' + item + '\n')

    with open(gitignore_file, 'r', encoding='utf-8') as f:
        ignore_list = f.read().splitlines()

    open(output_file, 'w', encoding='utf-8').close()

    print_directory_structure(ignore_list=ignore_list)


if __name__ == "__main__":
    run_script()
