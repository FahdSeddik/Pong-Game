import turtle #alternative is pygame
import winsound



wn = turtle.Screen()
wn.title("Pong by Fahood")
wn.bgcolor("black")
wn.setup(width=800, height=600) #(0, 0) is located at center of screen width is x & horizontal height is y & vertical
wn.tracer(0)


#Score
score_a = 0
score_b = 0

#Sounds
#ballsound = "bounce.wav"  #you can use "filename.type" instead of ballsound definition

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") #default is 20x20 pixels
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") #default is 20x20 pixels
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") #default is 20x20 pixels
ball.color("white") 
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15   #you have to move the ball inside main game loop

# Pen (it is a turtle object within the turtle)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
# cant put write here or not update 
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #check write function for details

#Functions
    #paddle_a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

    #paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Keyboard binding
wn.listen()
    #paddle_a
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
    #paddle_b
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor()>=300:
        ball.sety(300) #to avoid some problems
        ball.dy *= -1

    if ball.ycor()<=-300:
        ball.sety(-300)
        ball.dy *= -1


    if ball.xcor()>=400:
        ball.setx(0) #return ball to center
        ball.dx *= -1
        score_a += 1
        #have to clear
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #check write function for details

    if ball.xcor()<=-400:
        ball.setx(0)
        ball.dx *= -1
        score_b += 1
        #have to clear
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #check write function for details

    # Paddle Hitting
    if (ball.ycor()>=paddle_a.ycor()-40) and (ball.ycor()<=paddle_a.ycor()+40) and (ball.xcor()>=-350) and (ball.xcor()<=-340):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('D:\\Programming\\Python\\Games\\Pong\\bounce.wav', winsound.SND_ASYNC) #you can use "filename.type" instead of ballsound definition
 
    if (ball.ycor() >= paddle_b.ycor()-40) and (ball.ycor() <= paddle_b.ycor()+40) and (ball.xcor()>=340) and (ball.xcor()<=350):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('D:\\Programming\\Python\\Games\\Pong\\bounce.wav', winsound.SND_ASYNC)
