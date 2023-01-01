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
    ## print(*num_list, sep = ", ")
    return num_list

## returns next number in sequence
def collatz_helper(num):
    if (num % 2 == 0):
        return int(num / 2)
    else:
        ## the edmund harris one uses / 2 for some reason???
        return int((3 * num + 1) / 2)

def collatz_visualization_animated(end):
    ## change angle & length to modify visualization
    length = 5
    angle = 5
    my_origin = (0, 0)
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
        turtle.setposition(my_origin)
        turtle.pendown()
        for i in collatz_seq:
            if (i % 2 == 0):
                turtle.right(angle)
            else:
                turtle.left(angle) 
            turtle.forward(length)
    ## prevents window from automatically closing 
    turtle.done()

def collatz_visualization(end):
    ## change angle & length to modify visualization
    length = 5
    angle = 5
    my_origin = (0, 0)
    ## turtle settings
    turtle.degrees()
    turtle.pencolor("#045a87")
    turtle.pensize(1.1)
    turtle.bgcolor(0, 0, 0)
    turtle.tracer(False) #skips tracer animation to speed up code
    ## draws a line depending on collatz seq for each number
    for num in range (end):
        collatz_seq = collatz(num)
        ## set position of turtle back to origin (does not reset direction of turtle)
        turtle.penup()
        turtle.setposition(my_origin)
        turtle.pendown()
        for i in collatz_seq:
            if (i % 2 == 0):
                turtle.right(angle)
            else:
                turtle.left(angle) 
            turtle.forward(length)
    ## prevents window from automatically closing 
    turtle.done()

def collatz_harris_visualization(end):
    ## change angle & length to modify visualization
    length = 10
    angle = 0.08
    my_origin = (-400, -400)
    ## turtle settings
    turtle.radians()
    turtle.pencolor("#045a87")
    turtle.bgcolor(0, 0, 0)
    turtle.tracer(False) #skips tracer animation to speed up code
    # turtle.pensize(1.1)
    ## draws a line depending on collatz seq for each number
    for num in range (end):
        collatz_seq = collatz(num)
        ## set position of turtle back to origin (does not reset direction of turtle)
        turtle.penup()
        turtle.setposition(my_origin)
        turtle.setheading(3.141)
        turtle.pendown()
        for i in range (len(collatz_seq) - 1):
            if (collatz_seq[i + 1] == 2 * collatz_seq[i]):
                turtle.right(2 * angle)
            else:
                turtle.left(angle) 
            turtle.forward(length)
    ## prevents window from automatically closing 
    turtle.done()

if __name__ == '__main__':
    ## collatz_visualization(4000) ## faster but not animated
    ## collatz_visualization_animated(1000) ## animated but takes much longer
    collatz_harris_visualization(4000) ## edmund harris visualization