import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll

while True:
    players=input("Enter the number of players(2-4):")
    if players.isdigit():
        players=int(players)
        if players>=2 and players<=4:
            break
        else:
            print("Players no must be between 2-4!")

    else:
        print("Invalid try again.")

max_score=50
player_score=[0 for _ in range(players)]   

while max(player_score)<max_score:
    for player_ind in range(players):
        print("\nPlayer number",player_ind+1,"turn has just started!")
        print("Your total score is:",player_score[player_ind],"\n")
        current_score=0

        while True:
         should_roll= input("Would you like to roll")
         if should_roll.lower()!='y':
            break

         value=roll()
         if value==1:
            print("You rolled a 1! Turn done!")
            current_score=0
            break
         else:
            current_score+=value
            print("You rolled:",value)
         print("Your score is:",current_score)

    player_score[player_ind]+=current_score
    print("Your total score is:",player_score[player_ind])
max_score=max(player_score)
winning_ind=player_score.index(max_score)
print("player number",winning_ind+1,"is th winner with the score of:",max_score)               
        
