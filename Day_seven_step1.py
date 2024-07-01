import random
import Day_seven_hangman_dic
import Day_seven_practice

stages = Day_seven_practice.stages_list
words = Day_seven_hangman_dic.word_list
choosen_word = random.choice(words)
logo = Day_seven_practice.logo
display = []
num_of_lives = 6
print(logo)

word_lenght = len(choosen_word)

for _ in range(word_lenght):
    display += "_"
continue_ = display != list(choosen_word)
while continue_:
    guess = input("Guess a letter : ").lower()
    for position in range(word_lenght):
        letter = choosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in choosen_word:
        num_of_lives -= 1
    if num_of_lives < 1:
        continue_ = False

    print(stages[num_of_lives])
    print(display)
if num_of_lives == 0:
    print("You lose")
    print(f"The word is{choosen_word}")
else:
    print("You win")
    print(f"The word is{choosen_word}")
