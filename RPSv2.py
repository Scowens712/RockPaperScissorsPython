import random

score = 0
opponent = 0

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")

elif user_action == "rock" and computer_action == "scissors":
        print("Rock beats scissors! You win Round 1!")
        score = score+1
elif user_action == "paper" and computer_action == "rock":
        print("Paper beats rock! You win Round 1!")
        score = score+1
elif user_action == "scissors" and computer_action =="paper":
        print("Scissors beats paper! You win Round 1!")
        score = score+1
else:
    print("You lose Round 1!")
    opponent = opponent+1
    

print("Your current score is",score)
print("Computer score is", opponent)

        


#User will be given the option to play a 2nd round



user_action = input("Do you wish to continue? Type 'start' for next round")
possible_actions = ["start"]

if user_action == "start":

    print("Let the Games Begin...")

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")

elif user_action == "rock" and computer_action == "scissors":
        print("Rock beats scissors! You win Round 2!")
        score = score+1
elif user_action == "paper" and computer_action == "rock":
        print("Paper beats rock! You win Round 2!")
        score = score+1
elif user_action == "scissors" and computer_action =="paper":
        print("Scissors beats paper! You win Round 2!")
        score = score+1
else:
    print("You lose Round 2!")
    opponent = opponent+1
    

print("Your current score is",score)
print("Computer score is", opponent)


#User will play a 3rd round

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")

elif user_action == "rock" and computer_action == "scissors":
        print("Rock beats scissors! You win Round 3!")
        score = score+1
elif user_action == "paper" and computer_action == "rock":
        print("Paper beats rock! You win Round 3!")
        score = score+1
elif user_action == "scissors" and computer_action =="paper":
        print("Scissors beats paper! You win Round 3!")
        score = score+1
else:
    print("You lose Round 3!")
    opponent = opponent+1
    

print("Your current score is",score)
print("Computer score is", opponent)

#User will be given the option to play a 4th round

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")

elif user_action == "rock" and computer_action == "scissors":
        print("Rock beats scissors! You win Round 4!")
        score = score+1
elif user_action == "paper" and computer_action == "rock":
        print("Paper beats rock! You win Round 4!")
        score = score+1
elif user_action == "scissors" and computer_action =="paper":
        print("Scissors beats paper! You win Round 4!")
        score = score+1
else:
    print("You lose Round 4!")
    opponent = opponent+1
    

print("Your current score is",score)
print("Computer score is", opponent)

#User will be given the option to play a 5th round

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")

elif user_action == "rock" and computer_action == "scissors":
        print("Rock beats scissors! You win Round 5!")
        score = score+1
elif user_action == "paper" and computer_action == "rock":
        print("Paper beats rock! You win Round 5!")
        score = score+1
elif user_action == "scissors" and computer_action =="paper":
        print("Scissors beats paper! You win Round 5!")
        score = score+1
else:
    print("You lose Round 5!")
    opponent = opponent+1
   
print("Your final score is",score)
print("Computer final score is", opponent)

if score > opponent:
    print("Game Over, you are the champion!!!")
elif score == opponent:
    print("It's a Draw, Stand Down!!")
else:
    print("Game Over, you lost to the computer")
