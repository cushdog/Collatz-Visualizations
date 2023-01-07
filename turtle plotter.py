import turtle
import tkinter
from math import *
from random import randint
from PIL import Image
import matplotlib.pyplot as plt
import time

def collatz(num):
    list = []
    ## add current number to list and set num to next number in seq
    while num > 1:
        list.append(num)
        num = collatz_helper(num)
    ## loop breaks when num = 1 --> add 1 to list here
    list.append(1)
    return list
    
## returns next number in sequence
def collatz_helper(num):
    if (num % 2 == 0):
        return int(num / 2)
    else:
        return 3 * num + 1


def draw_tree(starting_num, even_angle, odd_angle):

    root = tkinter.Tk()
    root.geometry('500x500-5+40')
    cv = turtle.ScrolledCanvas(root, width=900, height=900)
    cv.pack()

    screen = turtle.TurtleScreen(cv)
    screen.screensize(2000,1500)
    t = turtle.RawTurtle(screen)
    t.hideturtle()
    t.speed(420)
    list = collatz(starting_num)

    t.pendown()
    for item in list:
        if (item % 2 == 0):
            t.right(even_angle) # angle for even needs to be smaller than odd
            t.forward(10)
        elif (item % 2 != 0):
            t.left(odd_angle) # angle for odd needs to be bigger than even
            t.forward(10)
    t.penup()
    t.home()

even_angle = 23
odd_angle = 42


x = 123984776876
print(x)
draw_tree(x, even_angle, odd_angle)
time.sleep(10)
ts = turtle.getscreen()
ts.getcanvas().postscript(file="duck.eps")