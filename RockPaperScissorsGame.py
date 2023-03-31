import random

choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)

print("Let's play Rock Paper Scissors!")
player_choice = input("Choose rock, paper or scissors: ")

print("You choose", player_choice)
print("The computer choose", computer_choice)

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock":
    if computer_choice == "paper":
        print("Computer wins!")
    else:
        print("You win!")
elif player_choice == "paper":
    if computer_choice == "scissors":
        print("Computer wins!")
    else:
        print("You win!")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("Computer wins!")
    else:
        print("You win!")
else:
    print("Invalid input")