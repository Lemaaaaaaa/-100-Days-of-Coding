import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Imports the game logo
print(hangman_art.logo)


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You have already guessed {guess}, please guess again")#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Checks if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the {chosen_word}, you lost a life buddy!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Joins all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Checks if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    hangman_pics=hangman_art.stages
    print(hangman_pics[lives])
