# WIP

import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words) # randomly choose words from imported list
    while '-' in word or '' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_words(words)
    word_letters = set(word) # keeps track of letters in word
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() # what letters user has guessed

    # getting user input
    while len(world_letters) > 0:
        # letters used
        print('You have used these letters: ', ' '.join(used_letters))

        # what current word is:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
    
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
    
        else:
            print('Invalid character. Please try again.')


hangman()