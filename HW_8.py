'''GUESS THE NEMBER'''
import random
def guess_number():
    attempts = 0
    min_num = 1
    max_num = 100
    guessed = False
    print('Think of the numbers "yes, more, less"')
    while guessed is False:
        try:
            guess = random.randint(min_num, max_num)
            print(f"Is this number {guess}?")
            user_input = input().lower()

            if user_input == "y":
                guessed = True
                attempts += 1
                with open("results.txt", "a") as file:
                    file.write(f"The number was guessed in {attempts} attempts. Hidden number: {guess}.\n")
                print(f"The number was guessed in {attempts} attempts.")
            elif user_input == "m":
                with open("results.txt", "a") as file:
                    file.write(f'{attempts + 1}. {guess}\n')
                min_num = guess + 1
                attempts += 1
            elif user_input == "l":
                with open("results.txt", "a") as file:
                    file.write(f'{attempts + 1}. {guess}\n')
                max_num = guess - 1
                attempts += 1
            else:
                print('Please enter "yes, more, less".')
        except ValueError:
            print("'Don't cheat!")
            break
guess_number()
