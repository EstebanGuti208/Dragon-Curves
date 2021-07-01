import turtle
import time

t = turtle.Turtle()
t.speed(10)
t.up()
t.goto( 0, 0)
t.down()


def drawFractal(iterations, color):
    t.pencolor(color)
    turnList = [0]

    for i in range(1, iterations):
        partialList = turnList[0:]
        partialList.reverse()
        for y in range(len(partialList)):
            if partialList[y] == 1:
                partialList[y] = 0
            else:
                partialList[y] = 1
        turnList.append(0)
        turnList = turnList + partialList
    processMovement(turnList)

def processMovement(turns):
    
    for turn in turns:
        if turn == 0:
            t.forward(5)
            t.right(90)
           
        else:
            t.forward(5)
            t.left(90)
            



if __name__== '__main__':

    iterations = int(input("How many iterations do you want?"))
    t.up()
    t.setheading(0)
    t.down()
    drawFractal(iterations, 'green')
    t.up()
    t.setheading(90)
    t.goto(0, 0)
    t.down()
    drawFractal(iterations, 'blue')
    t.up()
    t.setheading(180)
    t.goto(0, 0)
    t.down()
    drawFractal(iterations, 'black')
    t.up()
    t.setheading(270)
    t.goto(0, 0)
    t.down()
    drawFractal(iterations, 'red')
    x = int(input('Do you want to go again?'))
    if x:
        t.forward(10)
    else:
        t.left(80)
    time.sleep(10)
 