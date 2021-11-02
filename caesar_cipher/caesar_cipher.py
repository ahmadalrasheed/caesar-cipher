from nltk.corpus import words, names
import nltk
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)


word_list = words.words()
name_list = names.words()

uppercase_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text_phrase, numeric_shift):
    text = ''
    for char in plain_text_phrase:
        if char in uppercase_letter:
            character = (uppercase_letter.index(char) + numeric_shift) % 26
            text += uppercase_letter[character]
        elif char in lowercase_letter:
            character = (lowercase_letter.index(char) + numeric_shift) % 26
            text += lowercase_letter[character]
        elif char not in uppercase_letter and char not in lowercase_letter:
            character = re.sub(r'[^A-Za-z]', ' ', char)
            text += character
    return text


def decrypt(plain_text_phrase, numeric_shift):

    return encrypt(plain_text_phrase, -numeric_shift)


def count_words(plain_text_phrase):
    """
    Counts the amount of english words in a string
    """
    # split the string into an array
    words = plain_text_phrase.split()
    word_count = 0
    for i in words:
        clean_word = re.sub(r'[^A-Za-z]', ' ', i)
        # check if each word is found in either the word list or name
        if clean_word.lower() in word_list or clean_word in name_list:
          # increment word count
            word_count += 1
    return word_count


def crack(plain_text_phrase):
    text = ''
    for i in range(26):
        total_words = decrypt(plain_text_phrase, i)
        word_count = count_words(total_words)
        ratio = word_count / len(total_words.split())
        percentage = int(ratio * 100)
        if percentage > 50:
            text += total_words
    return text