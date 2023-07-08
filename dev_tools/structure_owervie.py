import os


def run_script():
    root_directory = r'C:\Users\misty\PycharmProjects\PythonTeamFastAPI'
    output_file = 'folder_structure.txt'
    gitignore_file = r'C:\Users\misty\PycharmProjects\PythonTeamFastAPI\.gitignore'

    def print_directory_structure(directory=root_directory, indent=''):

        with open(output_file, 'a', encoding='utf-8') as file:
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):
                    if item in ignore_list:
                        continue
                    else:
                        file.write(indent + '├── ' + item + '/' + '\n')
                        print_directory_structure(item_path, indent + '│   ')
                else:
                    file.write(indent + '├── ' + item + '\n')

    with open(gitignore_file, 'r', encoding='utf-8') as f:
        ignore_list = f.read().splitlines()

    open(output_file, 'w', encoding='utf-8').close()

    print_directory_structure()


if __name__ == "__main__":
    run_script()
