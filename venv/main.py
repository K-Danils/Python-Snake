from turtle import Screen
import time
from food import Food
from Snake import Snake
from ScoreBoard import ScoreBoard

WIDTH = 600
HEIGHT = 600

distanceToFood = 25

def check_for_press():
    s.onkeypress(snake.up, "w")
    s.onkeypress(snake.down, "s")
    s.onkeypress(snake.right, "d")
    s.onkeypress(snake.left, "a")
    s.listen()


# Screen setup
s = Screen()
s.setup(WIDTH, HEIGHT)
s.title("Snake Game")
s.bgcolor("black")
s.tracer(0)

# Game object init
snake = Snake()
food = Food(WIDTH, HEIGHT)
scoreBoard = ScoreBoard()

head = snake.cubes[0]

while True:
    s.update()
    check_for_press()
    time.sleep(0.1)
    snake.move()
    
    if not snake.check_for_collision():
        scoreBoard.reset_score()
        snake.clear_snake()
        time.sleep(1)
        snake = Snake()
        
    if snake.cubes[0].distance(food) < 25:
        food.respawn()
        snake.grow()
        scoreBoard.increase_score()

scoreBoard.write_game_over()




s.exitonclick()
