import random
secret_number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

match guess:
    case _ if guess < secret_number:
        print("Nope, your guess is a bit low. Give it another shot!")
    case _ if guess > secret_number:
        print("Oops, your guess is a bit high. Try again!")
    case _:
        print("Congratulations! You guessed it!")

play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
    exec(open(__file__).read())
else:
    print("Thanks for playing!")