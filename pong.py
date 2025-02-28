import turtle

#creating the game window
window = turtle.Screen()
window.title("Pong by Mxolisi Khumalo")
window.bgcolor("grey")
window.setup(width=800, height=600)
window.tracer(0)

# player 1 paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)  #speed of animation, sets to maximum
paddle_1.shape("square") # set the paddle shape
paddle_1.shapesize(stretch_wid=5, stretch_len=1) # alter shape to desired size
paddle_1.color("blue")  # set paddle colour
paddle_1.penup()    # pen up removes the line that a turtle object draws
paddle_1.goto(-350, 0)  # set the paddle's initial position


# player 2 paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)  #speed of animation, sets to maximum
paddle_2.shape("square")    # set the paddle shape
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("red")
paddle_2.penup()
paddle_2.goto(+350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)  #speed of animation, sets to maximum
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)


# game functions
def paddle_1_up():
    y = paddle_1.ycor() # get the y cordinate of the object
    y += 20 # increment the y cordinate by 20 pixels to move it up
    paddle_1.sety(y)    # set the paddle to its new y value

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20 
    paddle_1.sety(y)    

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20 
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20 
    paddle_2.sety(y)   

# using the game functions using keyboard binding
window.listen() # tells the turtle window to listen for keyboard input
window.onkeypress(paddle_1_up, "w") # when w(without caps) is pressed call the function paddle_1_up
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")


# Main game loop
while True:
    window.update()