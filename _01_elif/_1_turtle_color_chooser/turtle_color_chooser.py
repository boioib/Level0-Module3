import random
import sys
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
 window = turtle.Screen()
 window.bgcolor('white')

 my_turtle=turtle.Turtle()
 my_turtle.width(10)


 while(True):
     color=simpledialog.askstring(title='Question',prompt='What color would you like to draw with?')








     for i in range(4):
        my_turtle.pencolor(color)

        if color ==(""):
            color=(get_random_color())
            break
        my_turtle.forward(50)
        my_turtle.left(360/4)


    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
 turtle.done()
