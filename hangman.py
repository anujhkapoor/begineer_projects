import random 
from words import words
import string
 
def get_valid_word(words):
    word = random.choice(words) #selects words from the list randomly 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print('You have',lives, 'lives left and you have used these letter: ',' '.join(used_letters))

        #What current word is 
        #word_list = [letter if letter in used_letters else '-' for letter in word]
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')
        print('Current word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in word')

        elif user_letter in used_letters:
            print('You have already used that character, please try again!')
        else:
            print('Invalid letter, please try again!')
    
    print('The word is :',word)

hangman()
