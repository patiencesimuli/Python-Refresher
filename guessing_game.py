secret_word = "intelligence"
user_guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while user_guess != secret_word:
    if (guess_count < guess_limit):
        user_guess = input ("Enter your guess: ")
        guess_count ++
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("You are out of guesses, GAME LOST")
else:
    print ("You win!")
