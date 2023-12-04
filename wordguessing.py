# ASSIGNMENT3
# student: Yildirim Bayazit Akyurek
# number : 21904343
# section: BBM103-1

import datetime
import os
import sys

# Command line arguments check. It should have at least two arguments.
while len(sys.argv) < 3:
    print('You must provide two arguments for this program')
    quit()

words_file = sys.argv[1]
letter_points_file = sys.argv[2]


# Function to create a dictionary from a text file
def create_dict(txt_file):
    dict_list = {}
    with open(txt_file, 'r', encoding='utf-8') as file:
        for line in file:
            key, val = line.replace('İ', 'i').replace('I', 'ı').lower().split(':')
            dict_list[key] = val.strip('\n')
    return dict_list


# Function to calculate and print the score of guessed words
def calculate_score(guessed_words_list, letters):
    total_score = 0
    for word in guessed_words_list:
        for letter in word:
            total_score += int(letter_value[letter]) * len(word)

    if total_score == 0:
        print(f'Score for {letters.upper()} is {total_score} and no words were guessed correctly.')
    else:
        print(f'Score for {letters.upper()} is {total_score} and guessed words are: {", ".join(guessed_words_list)}')


# Creating dictionaries from files
letter_value = create_dict(letter_points_file)
correct_words = create_dict(words_file)

# The game starts here
for shuffled_letters in correct_words.keys():
    start_time = datetime.datetime.now()
    time_count = 1
    game_word_list = [word.lower() for word in correct_words[shuffled_letters].split(',')]
    guessed_words = []

    print(f'Shuffled letters are: {shuffled_letters.replace("i", "İ").replace("ı", "I").upper()}')
    print('Please guess words for these letters with a minimum of three letters')

    while time_count <= 30:
        guessed_word = input('Guessed word: ').replace('İ', 'i').replace('I', 'ı').lower()

        is_valid_word = guessed_word in game_word_list
        already_guessed = guessed_word in guessed_words
        now_time = datetime.datetime.now()
        difference = now_time - start_time
        time_count = int(difference.seconds)

        if not is_valid_word:
            print('Your guessed word is not a valid word')
        elif already_guessed:
            print('This word has been guessed before')
        else:
            if time_count < 30:
                guessed_words.append(guessed_word)

        remaining_time = max(30 - time_count, 0)
        print(f'You have {remaining_time} seconds left')

        if time_count >= 30:
            print('You have run out of time')
            calculate_score(guessed_words, shuffled_letters)
            break
