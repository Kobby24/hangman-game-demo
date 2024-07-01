import random
word_list =["kobby", "gilbert", "effah"]
choosen_word = word_list[random.randint(0,2)]
print(choosen_word)
guess = input("Guess a letter\n").lower()
for i in choosen_word:
    if guess == i:
        print("Right")
    else:
        print("Wrong")

        