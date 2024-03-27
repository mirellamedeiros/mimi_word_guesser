import random


# let's define a function that will pick a word from a txt file we created
def mimi_word_picker(filename):
    with open(filename, 'r') as file:  # here the open() function is supposed to indeed open the file
        #  'r' is makes it so its in read-mode !
        words = file.readlines()  # this method takes the words from the txt file and puts them into the "words" list
    return random.choice(words).strip()  # and here it returns a random word from that list! the .strip() at the end
    # makes it so there are no extra blank spaces either before or after the word, which could be counted as characters
    # if I'm not mistaken !