
import random
choices = ("r", "p", "s")
emojis = {'r': "🪨", "p":"📃", "s":"✂️" }

while True:
    user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")

    elif (
    (user_choice == "r" and computer_choice == "s") or 
    (user_choice == "s" and computer_choice == "p") or 
    (user_choice == "r" and computer_choice == "p")):
        print("You win!")

    else:
        print("You lose!")

    play_again = input("Would you like to play again? (yes / no) : ").lower()

    if play_again == "no":
        print("Thank you for playing")
        break