#python3
from random      import randint
from sys         import argv
from random_word import RandomWords

def replace_helper(visible_items, target_word, user_guess):
    changes_made = False
    for index, letter in enumerate(target_word):
        if letter == user_guess:
            visible_items[index] = letter
            changes_made = True
    return changes_made


try:
    HANGMAN_SIZE = int(argv[1])
    WORD_SIZE = int(argv[2])
except:
    print("Usage: hangman rounds word_size. Using default number of rounds and word lengths..")
    HANGMAN_SIZE = 5
    WORD_SIZE = 5

R = RandomWords()
word = R.get_random_word(hasDictionaryDef='true', minLength=WORD_SIZE, maxLength=WORD_SIZE).lower()
char = word[randint(0, WORD_SIZE - 1)]
word_list = []
guess_list = [char]

for c in word:
    if c is char or not c.isalnum():
        word_list.append(c)
    else:
        word_list.append('_')

while(HANGMAN_SIZE > 0 or not word_list.count('_')):
    guess = input("Enter your guess! ")
    if guess not in guess_list and len(guess) == 1:
        guess_list.append(guess)
        if replace_helper(word_list, word, guess):
            print("Correct!")
            print("".join(word_list))
        else:
            HANGMAN_SIZE -= 1
            print("Wrong! You have", HANGMAN_SIZE, "guesses remaining.")
            print("".join(word_list))
    else:
        print("Invalid/Already used character. Try again.")
        print("".join(word_list))

print("\nThe word was", word)
