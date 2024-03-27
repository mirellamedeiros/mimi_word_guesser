from word_picker import mimi_word_picker


def guessing_game():
    word = str(mimi_word_picker('mimi_words.txt'))  # now we define from which file we want to take our words from!
    # the chosen word will be stored in the variable we created above !
    mysterious_word = '_' * len(word)  # here we define the letters-to-be-guessed as underscores times the length
    # of the chosen word (5 letters)
    wrong_letters = []
    tries = 6  # after 6 tries you lose!
    # right_letters = []  # here I will store the correct letters guessed, so I can update mysterious_word with them !!!

    print("˚ ༘♡ ⋆｡˚ welcome to mimi's guessing game ! ! ⋆.ೃ࿔*:･\nyou have 6 tries to guess a 5 letter word!\n˚₊· ➳❥ "
          "good luck! *:ꔫ:*+ﾟ\n" + "your word is: " + str(mysterious_word))

    # game rules:
    while tries > 0 and '_' in mysterious_word:
        current_try = input("feeling confident? try guessing a letter or a word! ").lower()  # match list lowercase

        if len(current_try) == 1 and current_try.isalpha():  # if the user tries a single letter

            if current_try in word:  # AND if the letter is correct
                for index, char in enumerate(word):
                    if char == current_try:
                        mysterious_word = mysterious_word[:index] + current_try + mysterious_word[index + 1:]
                        print("good job! ;)\n" + mysterious_word + "\nkeep going!")
                    else:
                        print("wrong guess! :( \n  previous tried letters are" + str(wrong_letters) + "\n"
                              + mysterious_word)
                        tries -= 1
                        wrong_letters.append(current_try)

            elif len(current_try) == len(word) and current_try.isalpha():  # if the user guesses the whole word at once!
                if current_try == word:
                    mysterious_word = word

                else:
                    print("that's not right! :(( \nlet's try again!")
                    tries -= 1

            else:
                print("that's not right!\n you have to guess a single letter or the entire word! ")

        if '_' not in mysterious_word:
            print("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ well done! you won!!!! ✧ﾟ･: *ヽ(◕ヮ◕ヽ)", word)
        else:
            print("(ಥ﹏ಥ) better luck next time! the word was: ", word)
