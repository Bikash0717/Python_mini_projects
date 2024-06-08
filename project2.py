import random

cwin=0
uwin=0

options=["rock","paper","scissor"]

while True:
    userin=input("Enter rock/paper/scissor or q to quit ").lower()
    if userin=='q':
        break
    if userin not in options:
        continue

    randomnum=random.randint(0,2)
    comin=options[randomnum]
    print("Computer pick="+comin)
    if userin=="rock" and comin=="scissor":
        print("You win!!!")
        uwin+=1
        continue
    elif userin=="paper" and comin=="rock":
        print("You win!!!")
        uwin+=1
    elif userin=="scissor" and comin=="paper":
        print("You win!!!")
        uwin+=1 
        continue 
    elif userin==comin:
        print("Tie!")  
    else:
        print("Computer wins!!!")
        cwin+=1
        continue

print("Final score is:")
print("Your score :",uwin,".")
print("Computer score:",cwin,".") 
if(uwin>cwin):
    print("You won the game!!!")
elif(cwin>uwin):
    print("You lost the game!!!")
else:
    print("Game is tied!!!")    
