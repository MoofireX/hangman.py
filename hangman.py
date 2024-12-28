#hangman.py

import turtle
import time
import random

t = turtle.Turtle()

body_count = 0

draw_pos = (-100.00,50.00)

def file(name=None):
    if name == None:
        words = open("/home/moofire/Desktop/Python/hangman_words.txt",'r')
        word_list = list(words)
    
    else:
        words = open(name,'r')
        word_list = list(words)

    return word_list

def indexes():
    indx_list = ["Head", "Body", "L_Arm", "R_Arm", "L_Leg", "R_Leg"]
    return indx_list


def draw_init(word = None):
    global draw_pos

    t.penup()
    t.right(90)
    t.backward(150)
    t.right(90)
    t.forward(50)
    t.pendown()
    t.penup()
    t.backward(200)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.pendown()
    t.right(90)
    t.pendown()
    t.forward(300)
    t.backward(150)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
        
    t.penup()

    return word

t.penup()
t.pendown()
t.right(180)

def draw_bodyparts(part):
    global body_count

    indx_list = indexes()
    current_indx = indx_list[part]

    if current_indx == "Head":
        t.circle(25)
        t.right(90)
        t.penup()

        body_count += 1

    elif current_indx == "Body":
        t.forward(5)
        t.pendown()
        t.forward(50)
        t.backward(25)
        t.penup()

        body_count += 1

    elif current_indx == "L_Arm":
        t.forward(30)
        t.pendown()
        t.right(45)
        t.forward(30)
        t.backward(30)
        t.left(45)
        t.penup()

        body_count += 1

    elif current_indx == "R_Arm":
        t.forward(30)
        t.pendown()
        t.left(45)
        t.forward(30)
        t.backward(30)
        t.right(45)
        t.penup()

        body_count += 1

    elif current_indx == "L_Leg":
        t.forward(55)
        t.pendown()
        t.right(45)
        t.forward(35)
        t.backward(35)
        t.left(45)

        body_count += 1

    elif current_indx == "R_Leg":
        t.forward(55)
        t.pendown()
        t.left(45)
        t.forward(35)
        t.backward(35)
        t.right(45)

        body_count += 1


def game():
    global xy,word,body_count, draw_pos, draw

    turn = 0
    win = None
    guess = ""

    print("This can be a 1-player or a 2-player game. 2-player mode needs a seperate word decider who doesn't play. That word decider will enter the word into the computer next.")

    porpp = input("Are you playing as a single player or as 2 players? Enter 1 for 1 player or 2 for 2 players: ")

    if porpp == "2":
        word = draw_init(input("What is the word? Shield this from the players: "))

        t.forward(350)
        t.left(90)
        t.backward(150)
        t.pendown()
    
        letters = list(word)
        xy = []

        for x in range(len(letters)):
            t.forward(25)
            xy.append(t.pos())
            t.forward(25)
            t.penup()
            t.forward(25)
            t.pendown()
    
    else:
        draw = 0
        print("For 1-player mode, the computer will generate a random word from the file of choosing. Please enter a file name for a customized word list, or enter 'None' to use the default file. The file is on the Github repository.")
        ask = input('What file would you like to use? ')
        if ask == "None":
            word_list = file()
        else:
            word_list = file(ask)

        input_word_indx = random.randint(0,len(word_list) - 1)
        word_p1 = word_list[input_word_indx]

        word = draw_init(word_p1)
        
        t.forward(350)
        t.left(90)
        t.backward(150)
        t.pendown()
    
        letters = list(word)
        xy = []

        for x in range(len(letters) - 1):
            t.forward(25)
            xy.append(t.pos())
            t.forward(25)
            t.penup()
            t.forward(25)
            t.pendown()

    if porpp == "2":
        print("p1 will go first. Let the hanging begin!")

        while win is None:

            if all(pos is None for pos in xy):
                print("p2 won!")
                break

            if turn == 0:
                print("p1's turn")
                guess = input("Guess a letter: ")

                if guess in word:
                    indx = word.index(guess)
                    t.penup()
                    t.goto(xy[indx])
                    for val in xy:
                        if xy[indx] is None:
                            indx -= 1
                    xy[indx] = None
                    t.pendown()
                    t.write(guess,font=("Arial",36,"normal"))
                    turn = 1
                else:
                    t.penup()
                    t.goto(draw_pos)
                    t.pendown()
                    draw_bodyparts(body_count)
                    
                    if body_count == 6:
                        time.sleep(1)
                        print("You caused the death of us all!! Including yourself of course.")
                        win = False                     

                    else:
                        turn = 1
                        continue

            elif all(pos is None for pos in xy):
                print("p1 won!")
                break


            elif turn == 1:
                print("p2's turn")
                guess = input("Guess a letter: ")

                if guess in word:
                    indx = word.index(guess)
                    t.penup()
                    t.goto(xy[indx])
                    xy[indx] = None
                    for val in xy:
                        if xy[indx] is None:
                            indx -= 1
        
                    t.pendown()
                    t.write(guess,font=("Arial",36,"normal"))
                    turn = 0
                else:
                    t.penup()
                    t.goto(draw_pos)
                    t.pendown()
                    draw_bodyparts(body_count)
                    
                    if body_count == 6:
                        time.sleep(1)
                        print("You caused the death of us all!! Including yourself of course.")
                        win = False

                    else:
                        turn = 0
                        continue

            elif all(pos is None for pos in xy):
                print("p2 won!")
                break
                    
            
    else:
        print("Let the hanging begin!")

        while win is None:

            if all(pos is None for pos in xy):
                print("You won!")
                break

            guess = input("Guess a letter: ")

            if guess in word_p1:
                indx = word.index(guess)
                t.penup()
                t.goto(xy[indx])
                for val in xy:
                    if xy[indx] is None:
                        indx -= 1
                xy[indx] = None
                t.pendown()
                t.write(guess,font=("Arial",36,"normal"))
                turn = 1
            else:
                t.penup()
                t.goto(draw_pos)
                t.pendown()
                draw_bodyparts(body_count)
                if body_count == 6:
                    time.sleep(1)
                    print("You've been hanged!")
                    win = False

                else:
                    continue

            if all(pos is None for pos in xy):
                print("You won!")
                break
                
if __name__ == "__main__":
    game()
