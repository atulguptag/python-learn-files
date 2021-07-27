print("Note: You have only 3 chance to choose the correct guess")

secreat_word = "harmonioum"
guess = ""
guess_count = 0
guess_limit = 3

out_of_guesses = False

while guess != secreat_word and not(out_of_guesses):

    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else :
        out_of_guesses = True

if out_of_guesses :
    print("Out_of_guesses, YOU LOSE THE GAME !")
else:
    print("You Win! ")









