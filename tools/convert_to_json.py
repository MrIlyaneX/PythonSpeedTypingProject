import json


async def convert_to_json(file_path: str, output_file_path: str):
    """
    Converter from txt to json, since json is more usable for fastapi requests
    
    :param file_path: 
    :param output_file_path: 
    :return: 
    """

    text = await reading_from_file(file_path)
    if text is not None:
        data = {"text": text}
        try:
            with open(output_file_path, 'w') as created_file:
                json.dump(data, created_file)
            print(f"File '{file_path}' converted to JSON and saved as '{output_file_path}'.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"File '{file_path}' not found.")


async def reading_from_file(path: str):
    try:
        with open(path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return None
    except Exception as e:
        return None
