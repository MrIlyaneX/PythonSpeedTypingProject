"""
    Version 1.0.0
    Very simple random-base text generator.

    Last modified 2021-04-20

    Generate random text based on a language's most common words.

    Generate random punctuation.
    Generate random phone numbers.
    Generate random digits.
"""

import json
import random


def get_words_lens(language: str = "en"):
    """
    Retrieves the lengths of words from a language-specific JSON file.

    :param language: The language code to specify the JSON file. Defaults to "en".
    :return: List[int]: A sorted list of unique word lengths.
    :raise "FileNotFoundError: If the JSON file for the specified language is not found.
    """
    with open(f'../data/words/{language}.json', 'r') as f:
        data = json.load(f)

    words = data['text'].split('\n')
    words_len = []
    for word in words:
        if len(word) not in words_len:
            words_len.append(len(word))

    words_len.sort()
    return words_len


def create_len_dict(language: str = "en"):
    """
    Creates a length dictionary for words in a specific language and saves it to a JSON file.
    - Retrieves the lengths of words from a language-specific JSON file using the get_words_lens function.
    - Creates a dictionary len_dict with the language as the key and the word lengths as the value.
    - Saves the len_dict to a JSON file named "{language}_len.json" in the "../data/words/" directory.

    :param language: The language for which the length dictionary is created. Defaults to "en".
    :return: None
    :raise FileNotFoundError: If the language-specific JSON file is not found.
    """
    words_len = get_words_lens(language)

    len_dict = {language: words_len}

    with open(f'../data/words/{language}_len.json', 'w') as f:
        json.dump(len_dict, f, indent=4)


def generate_pseudo_phone_number():
    """
    Generates a pseudo-random phone number in the format "XXX-XXX-XXXX".
    Note:
    - This function generates a pseudo-random phone number using random integers for the area code, first three digits,
        and last four digits.
    - The area code is a three-digit number ranging from 100 to 999.
    - The first three digits are also a three-digit number ranging from 100 to 999.
    - The last four digits are a four-digit number ranging from 1000 to 9999.
    - The generated phone number follows the format "XXX-XXX-XXXX", where each X represents a digit.

    :return: str: A pseudo-random phone number in the format "XXX-XXX-XXXX".
    """
    area_code = str(random.randint(100, 999))
    first_three_digits = str(random.randint(100, 999))
    last_four_digits = str(random.randint(1000, 9999))
    return f"{area_code}-{first_three_digits}-{last_four_digits}"


def generate_text(language: str = "en", use_punctuation: bool = False, digits: bool = False,
                  phone_number: bool = False):
    """
    Generates random text based on a language-specific word list and optional settings.

    Note:

    - Reads the language-specific word list from a JSON file named "{language}.json" in "../data/words/" directory.
    - Reads the length dictionary for the language from a JSON file "{language}_len.json" in "../data/words/" directory.
    - Shuffles the words from the word list.
    - Generates a random number of sentences (between 3 and 12).
    - Each sentence has a random length (between 4 and 15 words).
    - Adds common words specific to the English language.
    - Adds random digits if the digits parameter is True.
    - Adds a pseudo-random phone number if the phone_number parameter is True.
    - Capitalizes the first letter of each sentence and adds punctuation if the use_punctuation parameter is True.
    - Prints the generated text to the console.

    :param language: The language for which the text is generated. Defaults to "en".
    :param use_punctuation: Whether to include punctuation marks in the generated text. Defaults to False.
    :param digits: Whether to include random digits in the generated text. Defaults to False.
    :param phone_number: Whether to include a pseudo-random phone number in the generated text. Defaults to False.
    :return: None
    """
    with open(f'../data/words/{language}.json', 'r') as f:
        data = json.load(f)

    with open(f'../data/words/{language}_len.json', 'r') as f:
        len_data = json.load(f)

    words = data['text'].split('\n')
    word_lens = len_data[language]

    random.shuffle(words)

    sentences = []

    common_words = []

    if language == "en":
        common_words = ["and", "the", "is", "with", "to", "of", "in", "for", "it", "on", "that", "are", "was", "as",
                        "be", "from", "has", "by", "at"]

    for _ in range(random.randint(3, 12)):
        sentence_length = random.randint(4, 15)
        sentence_words = [random.choice(words) for _ in range(sentence_length)]
        sentence_words.append(common_words[random.randint(0, len(common_words) - 1)])

        # Add random digits if needed
        if digits and random.randint(0, 1):
            sentence_words.append(str(random.randint(0, 100)))
            if random.randint(0, 1) and random.randint(0, 1):
                sentence_words.append(str(random.randint(0, 100)))
            random.shuffle(sentence_words)

        if phone_number and random.randint(0, 1):
            sentence_words.append(generate_pseudo_phone_number())
            sentence_words.append(random.choice(words))

        sentence = ' '.join(sentence_words)

        # Capitalize first letter and add punctuation
        if use_punctuation:
            punctuation = random.choice(['.', ',', '.', ',', '!', '?'])
            sentence += punctuation

        if sentences and "," in sentences[-1]:
            sentence = sentence.lower()
        elif use_punctuation:
            sentence = sentence.capitalize()
        sentences.append(sentence)

    for sentence in sentences:
        print(sentence, end=" ")
    print()


if __name__ == '__main__':
    # create_len_dict("en")
    for _ in range(10):
        generate_text("en", use_punctuation=True, digits=False, phone_number=False)
        print()
