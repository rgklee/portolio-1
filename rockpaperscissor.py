#ruben
#1/7/2025
#rock paper scissors

#init
import random
win = 0
tie = 0
lose = 0
#function
def rps():
    global win
    global tie
    global lose
    while True:
        player = input("Rock, Paper, Scissors, Go: ")
        if player == "rock":
            print("Your move is Rock")
        elif player == "paper":
            print("Your move is Paper")
        elif player == "scissors":
            print("Your move is Scissors")

        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("The computer's move is Rock")
        elif computer == 2:
            computer = "paper"
            print("The computer's move is Paper")
        elif computer == 3:
            computer = "scissors"
            print("The computer's move is Scissors")

        if player.lower() == "rock" and computer == "rock":
            print("It is a tie!")
            tie = tie + 1
            print(win)
            print(tie)
            print(lose)
        elif player.lower() == "scissors" and computer == "scissors":
            print("It is a tie!")
            tie = tie + 1
            print(win)
            print(tie)
            print(lose)
        elif player.lower() == "paper" and computer == "paper":
            print("It is a tie!")
            tie = tie + 1
            print(win)
            print(tie)
            print(lose)
        elif player.lower() == "rock" and computer == "scissors":
            print("You win!")
            tie = tie + 1
            print(win)
            print(tie)
            print(lose)
        elif player.lower() == "paper" and computer == "rock":
            print("You win!")
            win = win + 1
            print(win)
            print(tie)
            print(lose)
        elif player.lower() == "scissors" and computer == "paper":
            print("You win!")
            win = win + 1
            print(win)
            print(tie)
            print(lose)
        elif player.lower() == "rock" and computer == "paper":
            print("The computer win!")
            win = win + 1
            print(win)
            print(tie)
            print(lose)
        elif player.lower() == "paper" and computer == "scissors":
            print("The computer win!")
            lose = lose + 1
            print(win)
            print(tie)
            print(lose)
        elif player.lower() == "scissors" and computer == "rock":
            print("The computer win!")
            lose = lose + 1
            print(win)
            print(tie)
            print(lose)
        playagain = input("Would you like to play again")
        if playagain.lower() == "yes":
            print("restaring.....")
        else:
            print("Thank you for playing")
            print(win)
            print(tie)
            print(lose)
            break

#main
print("Welcome to Rock Paper Scissors")
print("Make your move!")
rps()
