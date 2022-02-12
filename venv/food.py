from turtle import Turtle
import random

class Food(Turtle):
    BUFFER = 50
    
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(1, 1)
        self.speed("fastest")
        
        self.move_to_random_position_on_field()


    def respawn(self):
        self.move_to_random_position_on_field()

        
    def move_to_random_position_on_field(self):
        self.goto(
            random.randint(-((self.width / 2) - self.BUFFER),
                           ((self.height / 2) - self.BUFFER)),
            random.randint(-((self.width / 2) - self.BUFFER),
                           ((self.height / 2) - self.BUFFER))
                           )
