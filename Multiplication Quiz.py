#Ruben
#1/9/2025

#Init
import random
right = 0
wrong = 0

#Functions
def multiplicationquiz():
    global right
    global wrong
    print("Prepare for this multiplication quiz..")
    print("Question 1 of 5")
    result1 = int(random.randint(1,10))
    result2 = int(random.randint(1,10))
    print("What is " + str(result1) +"*"+ str(result2))
    answer1 = result1 * result2
    player1ans = int(input("Your answer"))
    if player1ans == answer1:
        print("You got #1 right. The answer was " + str(answer1))
        right = right + 1
    else:
        print("You got #1 wrong. The answer was " + str(answer1))
        wrong = wrong + 1

    print("Question 2 of 5")
    result3 = int(random.randint(1,10))
    result4 = int(random.randint(1,10))
    print("What is " + str(result3) +"*"+ str(result4))
    answer2 = result3 * result4
    player2ans = int(input("Your answer"))
    if player2ans == answer2:
        print("You got #2 right. The answer was " + str(answer2))
        right = right + 1
    else:
        print("You got #2 wrong. The answer was " + str(answer2))
        wrong = wrong + 1

    print("Question 3 of 5")
    result5 = int(random.randint(1,10))
    result6 = int(random.randint(1,10))
    print("What is " + str(result5) +"*"+ str(result6))
    answer3 = result5 * result6
    player3ans = int(input("Your answer"))
    if player3ans == answer3:
        print("You got #3 right. The answer was " + str(answer3))
        right = right + 1
    else:
        print("You got #3 wrong. The answer was " + str(answer3))
        wrong = wrong + 1

    print("Question 4 of 5")
    result7 = int(random.randint(1,10))
    result8 = int(random.randint(1,10))
    print("What is " + str(result7) +"*"+ str(result8))
    answer4 = result7 * result8
    player4ans = int(input("Your answer"))
    if player4ans == answer4:
        print("You got #4 right. The answer was " + str(answer4))
        right = right + 1
    else:
        print("You got #4 wrong. The answer was " + str(answer4))
        wrong = wrong + 1

    print("Question 5 of 5")
    result9 = int(random.randint(1,10))
    result10 = int(random.randint(1,10))
    print("What is " + str(result9) +"*"+ str(result10))
    answer5 = result9 * result10
    player5ans = int(input("Your answer"))
    if player5ans == answer5:
        print("You got #5 right. The answer was " + str(answer5))
        right = right + 1
    else:
        print("You got #5 wrong. The answer was " + str(answer5))
        wrong = wrong + 1

    print("You got " + str(right) + " answers right.")
    print("You got " + str(wrong) + " answers wrong.")

#main
multiplicationquiz()
