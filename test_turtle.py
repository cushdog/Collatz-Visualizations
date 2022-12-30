import turtle

def collatz(num):
    num_list = []
    ## add current number to list and set num to next number in seq
    while num > 1:
        num_list.append(num)
        num = collatz_helper(num)
    ## loop breaks when num = 1 --> add 1 to list here
    num_list.append(1)
    num_list.reverse()
    print(*num_list, sep = ", ")
    return num_list

## returns next number in sequence
def collatz_helper(num):
    if (num % 2 == 0):
        return int(num / 2)
    else:
        return 3 * num + 1

def collatz_visualizer_animated(end):
    ## change angle & length to modify visualization
    length = 5
    angle = 5
    origin = (0, 0)
    ## turtle settings
    turtle.degrees()
    turtle.pencolor("red")
    turtle.pensize(1.1)
    ## draws a line depending on collatz seq for each number
    for num in range (end):
        collatz_seq = collatz(num)
        turtle.bgcolor(0, 0, 0)
        turtle.tracer(False) #skips tracer animation to speed up code
        ## set position of turtle back to origin (does not reset direction of turtle)
        turtle.penup()
        turtle.setposition(origin)
        turtle.pendown()
        for i in collatz_seq:
            if (i % 2 == 0):
                turtle.right(angle)
            else:
                turtle.left(angle) 
            turtle.forward(length)
    ## prevents window from automatically closing 
    turtle.done()

def collatz_visualizer(end):
    ## change angle & length to modify visualization
    length = 5
    angle = 5
    origin = (0, 0)
    ## turtle settings
    turtle.degrees()
    turtle.pencolor("red")
    turtle.pensize(1.1)
    turtle.bgcolor(0, 0, 0)
    turtle.tracer(False) #skips tracer animation to speed up code
    ## draws a line depending on collatz seq for each number
    for num in range (end):
        collatz_seq = collatz(num)
        ## set position of turtle back to origin (does not reset direction of turtle)
        turtle.penup()
        turtle.setposition(origin)
        turtle.pendown()
        for i in collatz_seq:
            if (i % 2 == 0):
                turtle.right(angle)
            else:
                turtle.left(angle) 
            turtle.forward(length)
    ## prevents window from automatically closing 
    turtle.done()

if __name__ == '__main__':
    ## collatz_visualizer(1000) ## faster but not animated
    collatz_visualizer_animated(500) ## animated but takes much longer