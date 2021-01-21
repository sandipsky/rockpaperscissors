import random
game = True
print("###Rock, paper and Scissors game by SandipSky##")
print("Your choices are rock, paper, scissors")
def playgame():
    win = None
    inp = (input("Enter your choice: ")).lower()
    options = ['rock', 'paper', 'scissors']
    sy = random.choice(options)
    if inp in options:
        print("Your choice: " + inp)
        print("Computer choice: "+ sy)
        if inp == 'rock' and sy == 'scissors':
            win = True
        elif inp == 'paper' and sy == 'rock':
            win = True
        elif inp == 'scissors' and sy == 'paper':
            win = True
        elif inp == sy:
            print("Its a tie.")
        else:
            print("Sorry! You lost")

        if win:
            print("Congrats! You won")
    else:
        print("Please enter a valid option")


while(game):
    playgame()
    x = input(("Do u want to play again?(Y/n) ")).lower()
    if x == 'y':
        game = True
    else:
        game = False



