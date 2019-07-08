# Hangman.
# Made by Oliver Bevan in July 2019.
import random

print("Welcome to hangman!")
menu_choice = 0
while menu_choice != 3:
    print("Please pick an option.")
    print("1. Begin game")
    print("2. Show rules")
    print("3. Exit")
    menu_choice = int(input())

    if menu_choice == 1:  # Begin game.
        print("Thinking of a word...")

        dictionary = open("words.txt", "r")
        word_list = []
        for line in dictionary:
            word_list.append(line)
        dictionary.close()
        word_to_guess = word_list[random.randint(0, len(word_list) - 1)]
        print("Let's begin.")
        user_has_won = False
        lives_remaining = 8
        matched_characters = [" "] * len(word_to_guess)
        while not user_has_won and lives_remaining > 0:
            for i in range(0, len(word_to_guess)):
                if matched_characters[i] is not " ":
                    print(matched_characters[i], end=" ")
                else:
                    print("_", end=" ")
            print(
                f"\n    Please enter a guess. ({lives_remaining} lives remaining)")
            guess = input()
            if len(guess) > 1:
                # User is guessing the word.
                if guess == word_to_guess:
                    user_has_won = True
                else:
                    lives_remaining -= 1
                    print("Sorry, that's not the correct word.")
            else:
                # User is guessing a letter.
                if guess in word_to_guess:
                    for i in range(0, len(word_to_guess)):
                        if word_to_guess[i] == guess:
                            matched_characters[i] = guess
                else:
                    print("Sorry, that's not in the word.")
                    lives_remaining -= 1
        if user_has_won:
            print("Congratulations! You got it.")
        else:
            print("Sorry, you lose!")
        print(f"The word was {word_to_guess}")
    elif menu_choice == 2:  # Show rules.
        print("How to play:")
        print("Hangman is a simple guessing game.")
        print("The computer thinks of a word. To win, you simply guess the word by suggesting letters.")
        print(
            "If you cannot guess the word within the maximum number of guesses, you lose.")
        print("Good luck!")
