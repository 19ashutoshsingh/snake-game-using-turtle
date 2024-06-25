from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.title("My Snake Game")


game_is_on = True
user_choice = None


def restart():
    global game_is_on, user_choice, snake, food, scoreboard
    game_is_on = False
    screen.clear()
    screen.bgcolor("black")
    screen.title("My Snake Game")

    user_choice = screen.textinput(title="Make your choice", prompt="1 for wall barriers, 2 for no wall barriers: ")

    border = Border()
    border.create_border()

    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(restart, "r")
    # screen.exitonclick()

    game_is_on = True
    run_game(user_choice)


def run_game(user_choice):
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        if user_choice == "1":
            # Detect collision with wall
            if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
                game_over()

        else:
            # Detect collision with wall and wrap around
            if snake.segments[0].xcor() > 280:
                snake.segments[0].setx(-280)
            elif snake.segments[0].xcor() < -280:
                snake.segments[0].setx(280)
            elif snake.segments[0].ycor() > 280:
                snake.segments[0].sety(-280)
            elif snake.segments[0].ycor() < -280:
                snake.segments[0].sety(280)

        # Detect collision with tail
        for segment in snake.segments:
            if segment == snake.segments[0]:
                pass
            elif snake.segments[0].distance(segment) < 10:
                game_over()


def game_over():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()


user_choice = screen.textinput(title="Make your choice", prompt="1 for wall barriers, 2 for no wall barriers: ")
border = Border()
border.create_border()

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(restart, "r")

run_game(user_choice)

screen.exitonclick()

