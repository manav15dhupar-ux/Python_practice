'''The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score!'''

# import random

# def game():
#     print("You are palying game...")
#     score=random.randint(1,100)

#     with open("highscore.txt") as f:
#         highscore=f.read()
#         if(highscore!=""):
#             hiscore=int(highscore)
#         else:
#             highscore=0
#     print(f"Your score: {score}")
#     if(score>highscore):
#         with open("highscore.txt","w") as f:
#             f.write(str(score))

#     return score
# game()

# import os
import random

def game():
    # Ensure highscore file exists
    # if not os.path.exists("highscore.txt"):
    #     with open("highscore.txt", "w") as f:
    #         f.write("0")
    
    print("You are playing game...")
    score = random.randint(1, 100)
    
    # Read current high score safely
    with open("highscore.txt") as f:
        highscore_str = f.read().strip()
        highscore = int(highscore_str) if highscore_str else 0
    
    print(f"Your score: {score}")
    
    if score > highscore:
        with open("highscore.txt", "w") as f:
            f.write(str(score))
        print(f"New high score: {score}!")
    else:
        print(f"High score remains: {highscore}")
    
    return score

# Run the game
game()
