import turtle
import time
import random

screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('light green')

turtle.speed(5)
turtle.pensize(5)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#food
apple = turtle.Turtle()
apple.speed(0)
apple.shape('circle')
apple.color('red')
apple.penup()
apple.goto(30,30)
old_apple=[]

#score
score = 0
delay = 0.15

scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :",align="center",font=("new times roman",22,"bold"))


# move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard 
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

while True:
        screen.update()
            
        if snake.distance(apple)< 20:
                x = random.randint(-290,270)
                y = random.randint(-240,240)
                apple.goto(x,y)
                scoring.clear()
                score+=1
                scoring.write("Score:{}".format(score),align="center",font=(" new times roman",22,"bold"))
                delay-=0.001
                
                #adding apples to snake
                new_fruit = turtle.Turtle()
                new_fruit.speed(0)
                new_fruit.shape('square')
                new_fruit.color('black')
                new_fruit.penup()
                old_apple.append(new_fruit)
        
        for index in range(len(old_apple)-1,0,-1):
                a = old_apple[index-1].xcor()
                b = old_apple[index-1].ycor()

                old_apple[index].goto(a,b)
                                     
        if len(old_apple)>0:
                a = snake.xcor()
                b = snake.ycor()
                old_apple[0].goto(a,b)
        snake_move()

        #snake border collision    
        if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('light green')
                scoring.goto(0,0)
                scoring.write("   GAME OVER !!\n Your Score is {}".format(score),align="center",font=("new times roman",30,"bold"))


        # snake collision
        for food in old_apple:
                if food.distance(snake) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('light green')
                        scoring.goto(0,0)
                        scoring.write("    GAME OVER !!\n Your Score is {}".format(score),align="center",font=("new times roman",30,"bold"))
                       


                
        time.sleep(delay)

turtle.Terminator()

