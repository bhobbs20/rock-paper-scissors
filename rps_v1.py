from random import randint 

player = input("Player, make your move: ").lower()
random_number = randint(0,2)
if random_number == 0:
    computer = "rock"
elif random_number == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")
    
