print("GuessTheWord (Угадай слово)") 
print("__________")
print("Привет! Загадано слово из случайной категории")
print("У тебя есть 4 попытки, чтобы угадать буквы, затем нужно ввести слово")
print("Получится ли у тебя угадать слово хоть раз?")
print("__________")

category1 = ["биология", "география", "информатика", "история", "литература", "математика", "музыка", "обществознание", "физика", "химия"]
category2 = ["компьютер", "принтер", "сканер", "монитор", "клавиатура", "мышь", "наушники"]
category3 = ["яблоко", "банан", "апельсин", "груша", "слива", "помидор", "огурец", "морковь", "картофель", "капуста", "лук", "перец", "кабачок"]
category4 = ["клубника", "малина", "ежевика", "смородина", "вишня", "черешня", "голубика", "брусника", "клюква", "земляника", "крыжовник", "черника"]
category5 = ["вода", "чай", "кофе", "молоко", "какао", "сок", "квас", "компот", "морс", "лимонад", "кисель", "кефир"]
category6 = ["парк", "школа", "больница", "магазин", "кафе", "кинотеатр", "музей", "пляж", "лес"]
categories = [(category1, "школьные предметы"), (category2, "техника"), (category3, "фрукты и овощи"), (category4, "ягоды"), (category5, "напитки"), (category6, "места")]

import random
chosen_list, category_name = random.choice(categories)
word = random.choice(chosen_list)
word_len = len(word)
popytki = 4
print(f"Категория: {category_name}")
print(f"Возможные слова: {chosen_list}")
print("__________")

i = "да"
while i == "да":
    if popytki != 0:
        letter_input = input("Введите букву (0 - если готовы ввести слово): ").lower()
        letter_input_len = len(letter_input)
        if letter_input_len == 1 and letter_input != "0":
            find = word.find(letter_input)
            if find >= 0:
                popytki -= 1
                print(f"✅ Буква {letter_input} ЕСТЬ в слове!")
                print("__________")
            elif find == -1:
                popytki -= 1
                print(f"❌ Буквы {letter_input} НЕТ в слове!")
                print("__________")
        elif letter_input_len == 1 and letter_input == "0":
                popytki = 0       
        else:
            print("❌ Долна быть введена одна буква!")
            print("__________")
            letter_input = 1
    else:
        print("Введите слово: ")
        word_input = input()
        print("__________")
        if word_input == word:
            print("🥳 Ура!")
            print("✅ Вы угадали слово!")
            print("__________")
            print("Хотите сыграть ещё раз?")
            print("да/нет")
            i = input().lower()
            print("__________")
            if i == "да":
                print("Новая игра")
                chosen_list, category_name = random.choice(categories)
                word = random.choice(chosen_list)
                word_len = len(word)
                popytki = 4
                print(f"Категория: {category_name}")
                print(f"Возможные слова: {chosen_list}")
                print("__________")
            elif i != "да":
                print("Игра окончена!")
        else:
            print("😥 Вы проиграли!")
            print(f"Слово: {word}")
            print("__________")
            print("Хотите сыграть ещё раз?")
            print("да/нет")
            i = input().lower()
            print("__________")
            if i == "да":
                print("Новая игра")
                chosen_list, category_name = random.choice(categories)
                word = random.choice(chosen_list)
                word_len = len(word)
                popytki = 4
                print(f"Категория: {category_name}")
                print(f"Возможные слова: {chosen_list}")
                print("__________")
            elif i != "да":
                print("Игра окончена!")
