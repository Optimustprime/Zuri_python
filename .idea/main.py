import random

while True:

    user_action = input("Enter a choice (R means rock,P means paper, S means scissors): ")
    # R="rock"
    # P="paper"
    # S="scissors"
    possible_actions = ['R', "P", "S"]
    computer_action = random.choice(possible_actions)
    if user_action in possible_actions:
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
        # print(user_action == computer_action)
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "R":
            if computer_action == "S":
                print("Rock smashes scissors! You win!")
                break
            else:
                print("Paper covers rock! You lose.Computer Wins")
                break
        elif user_action == "P":
            if computer_action == 'R':
                print("Paper covers rock! You win!")
                break
            else:
                print("Scissors cuts paper! You lose.Computer Wins")
                break
        elif user_action == "S":
            if computer_action == "P":
                print("Scissors cuts paper! You win!")
                break
            else:
                print("Rock smashes scissors! You lose.Computer Wins")
                break
        # game_options = input("Do you want to play again? (yes/no): ")
        # if game_options == "no":
        #     break
    else:
        print("Invalid Input")
