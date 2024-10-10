import random

options = ("rock", "paper", "scissors")

#computer to pick random choice from options
computer = random.choice(options)

#Ask player for input
player = input ("Enter a choice; rock, paper, or scissors:")

#Player can only choose options given
while player not in options:
    print("Please choose rock, paper or scissors.")
    player = input ("Enter a choice; rock, paper, or scissors:")

print(f"Player: {player}")
print(f"Computer: {computer}")

#checking for input and computer choice
if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "paper":
    print("You Loose!")
elif player == "scissors" and computer == "rock":
    print("You Loose!")
elif player == "paper" and computer == "scissors":
    print("You Loose!")
else: 
    print("You Win!")