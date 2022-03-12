print("=========Welcome to guess game=========")
secret_word = "apple"
guess = ""
guess_count = 0
guess_limit = 3

for i in range(guess_limit):
    if guess == secret_word:
        print("You win!")
        break
    else:
        guess = input("Enter guess: ")
        guess_count += 1
else:
    if guess == secret_word:
        print("You win!")
    else:
        print("You lose!")
        print("The secret word was:", secret_word)
