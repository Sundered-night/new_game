from .input import input
from .randomizer import ran

ran()
input()

def vic(player):
    if player == comp:
        print("THe game is a tie")
        
    elif player == "rock": 
        if comp == "paper":
            print("Paper loses to rock")
        else:
            print("Scissor wins")
    elif player == "paper":
        if comp == "scissor":
            print("Scissor beats paper")
        else:
            print("Rock beats paper")   
    elif player == "scissor":
        if comp == "rock":
            print("Rock beats scissor")
        else:
            print("Scissor beats paper")
    else:
        print("Lekhna aauna talai??")