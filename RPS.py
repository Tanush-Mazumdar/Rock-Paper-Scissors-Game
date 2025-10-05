import random
print ("the choices are : rock(R)","paper(P)","scissors(S)")
choices = ["R","P", "S"]
player_score = 0
computer_score = 0
print(", ".join(choices))
while True:
    player_Choice = input("Enter your choice ").upper() #function
    computer_choice = random.choice(choices) #--function
    print("Computer Choice: ",computer_choice)
    if player_Choice == computer_choice:
        print("It's a tie!")
    elif (player_Choice == "R" and computer_choice == "S") or (player_Choice == "S" and computer_choice== "P") or (player_Choice == "P" and computer_choice == "R"):
        print("You Win!")
        player_score +=1
    else:
        print("Computer Wins!")
        computer_score +=1
    print(f"Your Score = {player_score}\nComputer Score = {computer_score}")
    if player_score == 5:
        print("You win this round, you cheated")
        break
    elif computer_score==5:
        print("Computer wins this round")
        break