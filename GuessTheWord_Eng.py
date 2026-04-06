print("GuessTheWord")
print("__________")
print("Hello! A word from a random category has been chosen")
print("You have 4 attempts to guess letters, then you need to enter the word")
print("Will you be able to guess the word at least once?")
print("__________")

category1 = ["biology", "geography", "computer science", "history", "literature", "mathematics", "music", "social studies", "physics", "chemistry"]
category2 = ["computer", "printer", "scanner", "monitor", "keyboard", "mouse", "headphones"]
category3 = ["apple", "banana", "orange", "pear", "plum", "tomato", "cucumber", "carrot", "potato", "cabbage", "onion", "pepper", "zucchini"]
category4 = ["strawberry", "raspberry", "blackberry", "currant", "cherry", "sweet cherry", "blueberry", "lingonberry", "cranberry", "wild strawberry", "gooseberry", "bilberry"]
category5 = ["water", "tea", "coffee", "milk", "cocoa", "juice", "kvass", "compote", "fruit drink", "lemonade", "kissel", "kefir"]
category6 = ["park", "school", "hospital", "store", "cafe", "cinema", "museum", "beach", "forest"]
categories = [(category1, "school subjects"), (category2, "technology"), (category3, "fruits and vegetables"), (category4, "berries"), (category5, "drinks"), (category6, "places")]

import random
chosen_list, category_name = random.choice(categories)
word = random.choice(chosen_list)
word_len = len(word)
attempts = 4
print(f"Category: {category_name}")
print(f"Possible words: {chosen_list}")
print("__________")

again = "yes"
while again == "yes":
    if attempts != 0:
        letter = input("Enter a letter (0 - if you are ready to enter the word): ").lower()
        letter_len = len(letter)
        if letter_len == 1 and letter != "0":
            found = word.find(letter)
            if found >= 0:
                attempts -= 1
                print(f"✅ Letter {letter} IS in the word!")
                print("__________")
            elif found == -1:
                attempts -= 1
                print(f"❌ Letter {letter} is NOT in the word!")
                print("__________")
        elif letter_len == 1 and letter == "0":
            attempts = 0
        else:
            print("❌ You must enter one letter!")
            print("__________")
            letter = "1"  # to avoid issues, just a placeholder
    else:
        print("Enter the word: ")
        guess_word = input()
        print("__________")
        if guess_word == word:
            print("🥳 Hurray!")
            print("✅ You guessed the word!")
            print("__________")
            print("Do you want to play again?")
            print("yes/no")
            again = input().lower()
            print("__________")
            if again == "yes":
                print("New game")
                chosen_list, category_name = random.choice(categories)
                word = random.choice(chosen_list)
                word_len = len(word)
                attempts = 4
                print(f"Category: {category_name}")
                print(f"Possible words: {chosen_list}")
                print("__________")
            elif again != "yes":
                print("Game over!")
        else:
            print("😥 You lost!")
            print(f"The word was: {word}")
            print("__________")
            print("Do you want to play again?")
            print("yes/no")
            again = input().lower()
            print("__________")
            if again == "yes":
                print("New game")
                chosen_list, category_name = random.choice(categories)
                word = random.choice(chosen_list)
                word_len = len(word)
                attempts = 4
                print(f"Category: {category_name}")
                print(f"Possible words: {chosen_list}")
                print("__________")
            elif again != "yes":
                print("Game over!")