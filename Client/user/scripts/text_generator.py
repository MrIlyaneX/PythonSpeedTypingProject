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
import os
import random


def get_words_lens(language: str = "en"):
    """
    Get a list of word lengths for a language.
    Currently, do not used.

    :param language: Language to use. Currently only supports English.
    :return: List of word lengths.
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
    Create a dictionary of word lengths for a language.
    Currently, do not used.

    :param language: Language to use. Currently only supports English.
    :return: Dictionary of word lengths.
    """
    words_len = get_words_lens(language)

    len_dict = {language: words_len}

    with open(f'../data/words/{language}_len.json', 'w') as f:
        json.dump(len_dict, f, indent=4)


def generate_pseudo_phone_number():
    """
    Generate a pseudo phone number.

    :return: Pseudo phone number.
    """
    area_code = str(random.randint(1, 999))
    first_three_digits = str(random.randint(100, 999))
    last_four_digits = str(random.randint(1000, 9999))
    return f"{area_code}-{first_three_digits}-{last_four_digits}"


def generate_text(language: str = "en", use_punctuation: bool = False, digits: bool = False,
                  phone_number: bool = False):
    """
    Generate random text based on a language's most common words.

    :param language: Language to use. Currently only supports English.
    :param use_punctuation: Whether to use punctuation or not.
    :param digits: Whether to use digits or not.
    :param phone_number: Whether to use phone numbers or not.
    :return: Random text.
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    words_path = os.path.normpath(os.path.join(current_dir, "..", "data", "words", f"{language}.json"))
    len_path = os.path.normpath(os.path.join(current_dir, "..", "data", "words", f"{language}_len.json"))

    with open(words_path, 'r') as f:
        data = json.load(f)

    with open(len_path, 'r') as f:
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

    return sentences


if __name__ == '__main__':
    # create_len_dict("en")
    for _ in range(10):
        print(generate_text("en", use_punctuation=True, digits=False, phone_number=False))
