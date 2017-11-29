
from sys import exit
import random

food = [['Sushi', 'Japan'], ['Curry', 'India'], ['Currywurst', 'Germany'], ['Peking Duck', 'China'], ['Tom Yum Soup', 'Thailand'], ['Hotdog', 'USA']]

food_answered = []

def get_random_food_and_foodco():
    randint = random.randint(0, foodCount-1)
    food = foods[randint][0]
    foodco = foods[randint][1]
    while(food in foods_answered):
        randint = random.randint(0, foodCount-1)
        food = foods[randint][0]
        foodco = foods[randint][1]
    return food, foodco


if __name__ == "__main__":
    points = 0
    print "Hey there! This game is about guessing which country these foods came from!"
    foodCount = len(foods)
    print "There are %r foods to guess" % foodCount
    start = raw_input("Are you ready to start the game ? (yes|no)")
    if start == "no":
        print "OK BYE"
        exit(0)
    else:
        # Start the game
        name = raw_input("Tell me your name")
        print "Hurry up! %s guess the foods ! If you want to quit, press CTRL-C" % name
        while(True):
            food, foodco = get_random_food_and_foodco()
            print "This dish is called %s" % food
            print "Which country does this dish originate from?" % food
            answer = raw_input("Type the name of the country of %s : " % food)
            if answer.lower() == foodco.lower():
                points += 1
                foods_answered.append(food)
                print "Smartass, you're right!!"
                print "Your current score is %d" % points
                if(points == foodCount):
                    print "You maxed out your points in the game, good job! Thanks for playing"
                    exit(0)
            else:
                print "WRONG! WRONG!"
