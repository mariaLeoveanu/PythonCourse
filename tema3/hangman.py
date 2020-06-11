from words import words
import random


def get_random_word():
    return random.choice(words)


def game(word):
    guess = False
    guesses = []
    current_word = '_' * len(word)
    num_of_tries = 8
    print("Start game")
    print(current_word)
    print(word)
    while num_of_tries > 0 and not guess:
        inp = input("Enter letter or word: ").lower()
        if inp.isalpha():
            if len(inp) == 1 and inp.isalpha():
                if inp in guesses:
                    print("You guessed this letter before")
                elif inp in word:
                    print("Letter ", inp, " is part of the word")
                    list_word = list(current_word)
                    replace_indices = []
                    for idx, char in enumerate(word):
                        if char == inp:
                            replace_indices.append(idx)
                    for i in replace_indices:
                        list_word[i] = inp
                    current_word = "".join(list_word)
                    if "_" not in current_word:
                        guess = True
                    guesses.append(inp)
                else:
                    print("Letter ", inp, " is not part of the word")
                    num_of_tries -= 1
                    guesses.append(inp)
            elif inp.isalpha():
                if inp == word:
                    guess = True
                    current_word = word
                elif inp in guesses:
                    print("you guessed this word before")
                else:
                    print(inp, "is not correct")
                    num_of_tries -= 1
                    guesses.append(inp)
        else:
            print("Invalid input")
        print(current_word)
        print("Number of tries left: ", num_of_tries)
    if not guess:
        print("You lost! The word was", word)
    else:
        print("Congrats! You won!")


game(get_random_word())
