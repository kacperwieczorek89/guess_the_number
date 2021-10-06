from random import randint

def guess_the_number():
    number_to_guess = randint(1, 100)
    x = False
    while not x:
        try:
            given_number = int(input("Guess the number: "))
        except ValueError:
            print("It's not a number!")
            continue

        if number_to_guess == given_number:
            x = True
            print("You win!")
        elif number_to_guess < given_number:
            print("Too big!")
        elif number_to_guess > given_number:
            print("Too small!")

    return number_to_guess

guess_the_number()
