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
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("blue")
paddle_1.penup()
paddle_1.goto(-350, 0)


# player 2 paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)  #speed of animation, sets to maximum
paddle_2.shape("square")
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


# Main game loop
while True:
    window.update()