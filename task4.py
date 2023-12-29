import random
choices = ["Rock", "Paper", "Scissors"]
score = {"Wins": 0, "Losses": 0, "Draws": 0}
while True:
    user_choice_str = input("What do you choose? Type 'Rock', 'Paper', or 'Scissors'.\n").capitalize()
    user_choice = choices.index(user_choice_str) if user_choice_str in choices else -1

    computer_choice = random.choice(choices)

    print("You chose:", user_choice_str)
    print("Computer chose:", computer_choice)

    if user_choice == -1:
        print("Invalid choice, you lose!")
        score["Losses"] += 1
    else:
        if (
            (user_choice == 0 and computer_choice == "Scissors") or
            (user_choice == 1 and computer_choice == "Rock") or
            (user_choice == 2 and computer_choice == "Paper")
        ):
            print("You win!")
            score["Wins"] += 1
        elif (
            (computer_choice == "Rock" and user_choice == 2) or
            (computer_choice == "Paper" and user_choice == 0) or
            (computer_choice == "Scissors" and user_choice == 1)
        ):
            print("You lose!")
            score["Losses"] += 1
        else:
            print("It's a draw")
            score["Draws"] += 1

    print(f"Score: Wins - {score['Wins']}, Losses - {score['Losses']}, Draws - {score['Draws']}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
